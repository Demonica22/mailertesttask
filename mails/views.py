from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
from .models import Mail
from .forms import MailComposeForm
from users.models import User
import re
from copy import deepcopy


class InboxPage(generic.ListView):
    template_name = 'mails/inbox.html'
    context_object_name = 'inbox_page'

    def get(self, request):
        try:
            mails = Mail.objects.all().filter(receiver_id=request.user.id)
            mails = fullfill_mails(mails)
        except Mail.DoesNotExist:
            mails = []

        return render(request, self.template_name, {'mails': mails})


class SentMailsPage(generic.ListView):
    template_name = 'mails/inbox.html'
    context_object_name = 'sent'

    def get(self, request):
        try:
            mails = Mail.objects.all().filter(sender_id=request.user.id)
            mails = fullfill_mails(mails)
        except Mail.DoesNotExist:
            mails = []

        return render(request, self.template_name, {'mails': mails})


class MailDetailPage(generic.DetailView):
    template_name = 'mails/inbox.html'
    context_object_name = 'detail_page'

    def get(self, request, id):
        try:
            mail = [Mail.objects.get(id=self.kwargs["id"])]
            if mail[0].receiver.id == request.user.id:
                mail[0].was_read = True
                mail[0].save()
            mail = fullfill_mails(mail)
        except Mail.DoesNotExist:
            mail = None
        return render(request, self.template_name, {'mails': mail})


class MailComposePage(generic.CreateView):
    model = Mail
    template_name = "mails/mail_compose.html"
    form_class = MailComposeForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('mails:inbox'))

    def post(self, request):
        form = MailComposeForm(request.POST)
        if form.is_valid():
            receivers = request.POST.getlist('receivers')
            receivers = User.objects.filter(id__in=receivers)
            for receiver in receivers:
                mail_piece = deepcopy(form.save(commit=False))
                mail_piece.id = None
                mail_piece.receiver = receiver
                mail_piece.sender = request.user
                mail_piece.save()
        return HttpResponseRedirect(reverse('mails:inbox'))


def fullfill_mails(mails):
    # TODO: change default values of replacement
    regex = r"[%]\b.*\b[%]"
    for mail in mails:
        if re.search(regex, str(mail.text)):
            mail.text = mail.text.replace("%first_name%", mail.receiver.first_name or "default")
            mail.text = mail.text.replace("%last_name%", mail.receiver.last_name or "default")
            mail.text = mail.text.replace("%birthday%", str(mail.receiver.birth_date) or "default")
        if re.search(regex, str(mail.title)):
            mail.title = mail.title.replace("%first_name%", mail.receiver.first_name or "default")
            mail.title = mail.title.replace("%last_name%", mail.receiver.last_name or "default")
            mail.title = mail.title.replace("%birthday%", str(mail.receiver.birth_date) or "default")
    return mails

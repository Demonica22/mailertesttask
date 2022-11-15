from django.shortcuts import render
from django.views import generic
from .models import Mail


class InboxPage(generic.ListView):
    template_name = 'mails/inbox.html'
    context_object_name = 'inbox_page'

    def get(self, request):
        try:
            mails = Mail.objects.all().filter(receiver_id=request.user.id)
        except Mail.DoesNotExist:
            mails = []
        return render(request, self.template_name, {'mails': mails})


class MailDetail(generic.DetailView):
    template_name = 'mails/inbox.html'
    context_object_name = 'detail_page'

    def get(self, request, id):
        try:
            mail = [Mail.objects.get(id=self.kwargs["id"])]
            mail[0].was_read = True
            mail[0].save()
        except Mail.DoesNotExist:
            mail = None
        return render(request, self.template_name, {'mails': mail})

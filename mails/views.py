from django.shortcuts import render
from django.views import generic
from .models import Mail


class InboxPage(generic.ListView):
    template_name = 'mails/inbox.html'
    context_object_name = 'inbox_page'

    def get(self, request):
        print(request.user.id)
        try:
            mails = Mail.objects.all().filter(receiver_id=request.user.id)
        except Mail.DoesNotExist:
            mails = []
        print(mails)
        return render(request, 'mails/inbox.html', {'mails': mails})

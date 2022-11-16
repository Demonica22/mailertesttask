from django.urls import path
from . import views

app_name = 'mails'
urlpatterns = [
    path('inbox', views.InboxPage.as_view(), name='inbox'),
    path('sent', views.SentMailsPage.as_view(), name='sent'),
    path('<int:id>', views.MailDetailPage.as_view(), name='detail'),
    path('compose', views.MailComposePage.as_view(), name='compose'),
]

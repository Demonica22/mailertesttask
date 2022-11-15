from django.urls import path
from . import views

app_name = 'mails'
urlpatterns = [
    path('inbox', views.InboxPage.as_view(), name='inbox'),
    path('<int:id>', views.MailDetailPage.as_view(), name='detail'),
    #path('compose',views.)
]

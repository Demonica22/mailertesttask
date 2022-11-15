from django.urls import path
from . import views

app_name = 'mails'
urlpatterns = [
    path('inbox', views.InboxPage.as_view(), name='inbox'),
]

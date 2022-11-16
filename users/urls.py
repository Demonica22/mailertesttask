from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('<int:user_id>', views.user_profile_page, name='profile'),
    path("", include("django.contrib.auth.urls")),
]

from django.shortcuts import render
from .models import User
from django.http import Http404


def user_profile_page(request, user_id):
    template = "users/profile.html"
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, template, {'user': user})

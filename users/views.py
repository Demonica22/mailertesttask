from django.shortcuts import render
from .models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, reverse


def user_profile_page(request, user_id):
    template = "users/profile.html"
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, template, {'requested_user': user})


def user_login_page(request):
    template = 'users/login.html'
    if request.user.is_authenticated:
        return redirect("mails:inbox")
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect("mails:inbox")
            form.add_error("email", "Your password or email doesn't match")
        else:
            return render(request, template, {'form': form})

    else:
        form = UserLoginForm()
    return render(request, template, {'form': form})


def user_registration_page(request):
    if request.user.is_authenticated:
        return redirect("mails:inbox")
    template = "users/register.html"
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('users:login')
        return render(request, template, {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, template, {'user_form': user_form})


def user_logout_page(request):
    template = "users/logged_out.html"
    logout(request)
    return render(request, template)

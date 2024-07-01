from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth import logout

from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            user = form.instance
            auth.login(request, user)
            return redirect(reverse('main:index'))
    context = {
        'title': 'Registration',
    }
    return render(request, 'user/register.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('main:index'))
    context = {
        'title': 'Login',
    }
    return render(request, 'user/login.html', context)


@login_required(login_url='/')
def logout_user(request):
    logout(request)
    return redirect(reverse('main:index'))
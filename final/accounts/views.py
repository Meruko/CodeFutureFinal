from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Вы успешно зарегистрировались')

            return redirect('product_list')

        messages.error(request, 'Что-то пошло не так')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, 'Вы успешно авторизовались')

            if request.GET.get('next'):
                return redirect(request.GET.get('next'))

            return redirect('product_list')

        messages.error(request, 'Что-то пошло не так')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required()
def user_logout(request):
    logout(request)
    messages.warning(request, 'Вы вышли из аккаунта')
    return redirect('log in')

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control s-bg-sec-light', }),
        min_length=2
    )
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control s-bg-sec-light', }),
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control s-bg-sec-light', }),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control s-bg-sec-light', }),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control s-bg-sec-light', }),
        min_length=2
    )
    password = forms.CharField(
        label='Ваш пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control s-bg-sec-light', }),
    )
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import NewsBD
from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NewsBDForm(ModelForm):
    class Meta:
        model = NewsBD
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Заголовок'}),
            'anons': TextInput(attrs={'placeholder': 'Анонс'}),
            'content': Textarea(attrs={'placeholder': 'Текст'}),
            'date': DateTimeInput(attrs={'placeholder': 'Дата и время'})
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget= forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget= forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'}))

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'form-control'}))
    password2 = forms.CharField(label="Повтор", widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'form-control'}))
    email = forms.EmailField(label="Почта", widget=forms.EmailInput(attrs={'placeholder': '', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class ContactForm(forms.Form):
    recipient = forms.EmailField(
        label='Получатель',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    subject = forms.CharField(
        label='Заголовок письма',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    content = forms.CharField(
        label='Текст письма',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )
from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    sender = forms.CharField(widget=forms.HiddenInput(), required=False)
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control s-bg-sec-light', 'placeholder': 'Сообщение'}), required=True)

    class Meta:
        model = Message
        fields = ('sender', 'text')

class RoomForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2 s-bg-sec-light'}),
                           label='Название комнаты')

    class Meta:
        model = Room
        fields = ('name',)

class RoomInviteForm(forms.ModelForm):
    invite_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2 s-bg-sec-light'}),
                                  label='Код приглашения')

    class Meta:
        model = Room
        fields = ('invite_code',)

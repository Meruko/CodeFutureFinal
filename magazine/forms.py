from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'FIO_customer': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'deliver_address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date_finish': forms.DateTimeInput(attrs={
                'class': 'form-control'
            })
        }
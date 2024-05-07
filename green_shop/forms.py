from django import forms
from .models import Green

class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(BootstrapForm):
    class Meta:
        model = Green
        fields = [
            'name',
            'description',
            'price',
            'category',
            'photo'
        ]

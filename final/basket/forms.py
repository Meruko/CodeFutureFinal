from django import forms


class BasketAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Количество', widget=forms.NumberInput(attrs={'class': 'form-control'}))
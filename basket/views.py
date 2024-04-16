from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from magazine.models import Product
from .basket import Basket
from .forms import BasketAddProductForm

# Create your views here.
def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            quantity=form.cleaned_data['quantity'],
            update_quantity=form.cleaned_data['update']
        )
    return redirect('basket_detail')

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Order, Pos_order
from .basket import Basket
from .forms import BasketAddProductForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            quantity=form.cleaned_data['quantity']
        )
    return redirect('basket')


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.remove(product)
    messages.success(request, f'Товар {product.name} удалён из корзины!')
    return redirect('basket')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    messages.success(request, 'Корзина очищена!')
    return redirect('basket')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})


@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        messages.warning(request, 'Корзина пуста!')
        return redirect('basket')

    customer = request.user
    order = Order.objects.create(customer=customer)
    order.price = basket.get_total_price()
    message = f'<h1>Заказ №{order.pk}</h1><ul>'
    for item in basket:
        pos_order = Pos_order.objects.create(
            product=item['product'],
            count=item['quantity'],
            order=order
        )
        message += f'<li>{pos_order.product.name} ({pos_order.count} шт.) - {pos_order.sum_pos_order()} руб.</li>'
    message += f'</ul><p>Всего: {order.price} руб. ({basket.__len__()} шт.)</p>'

    basket.clear()
    messages.success(request, 'Заказ успешно оформлен!')
    send_mail(
        subject=f'Заказ №{order.pk}',
        message='',
        html_message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[customer.email],
        fail_silently=True
    )
    return redirect('basket')

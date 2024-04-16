from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from .models import Order, Supplier, Supply, Product
from .forms import OrderForm
from django.urls import reverse_lazy

from basket.forms import BasketAddProductForm
# Create your views here.
class OrderList(ListView):
    model = Order
    allow_empty = True

    def get_queryset(self):
        return Order.objects.order_by('-date_create')

    # @method_decorator(permission_required('magazine.view_order'))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

class OrderDetail(DetailView):
    model = Order

class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm

    extra_context = {
        'action': 'Создать'
    }

    @method_decorator(permission_required('magazine.add_order'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm

    extra_context = {
        'action': 'Изменить'
    }

    @method_decorator(permission_required('magazine.change_order'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')

    @method_decorator(permission_required('magazine.delete_order'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# ------------- Pract 2 -----------------
from rest_framework import viewsets
from .serializers import SupplierSerializer, SupplySerializer, ProductSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer

# -----------------------------------------
class ProductList(ListView):
    model = Product
    allow_empty = True

class ProductDetail(DetailView):
    model = Product
    extra_context = {
        'form_basket': BasketAddProductForm
    }

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def template_tags_django(request):
    context = {
        'html_code': '<p>Работа экранирования</p>',
        'var1': None,
        'var2': False,
        'var3': 0,
        'var4': '',
        'var5': '123546789',
        'some_list': ['Первый элемент', 'Второй элемент', 'Третий элемент',
                      'Ещё какой-то элемент', 'Последний элемент'],
        'some_list_empty': [],
        'obj': Product.objects.get(pk=1)
    }
    return render(request, 'magazine/tags/tags.html', context=context)
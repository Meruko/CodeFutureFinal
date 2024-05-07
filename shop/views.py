from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy

from .forms import ProductForm
from basket.forms import BasketAddProductForm
from .models import Product, Order
from .utils import paginate_elided


class ProductListView(ListView):
    model = Product
    allow_empty = True
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        paginate_elided(context)
        return context


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'form_basket': BasketAddProductForm
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'action': 'Создать'
    }

    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'action': "Изменить"
    }

    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class OrderListView(ListView):
    model = Order
    allow_empty = True
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        paginate_elided(context)
        return context

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-date_create')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

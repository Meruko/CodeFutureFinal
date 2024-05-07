from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .models import Green, Order
from .utils import *
from .forms import ProductForm
from basket.forms import BasketAddProductForm

class GreenListView(ListView):
    model = Green
    allow_empty = True
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        paginate_elided(context)
        return context


class GreenCreateView(CreateView):
    model = Green
    form_class = ProductForm

    extra_context = {
        'action': 'Создать'
    }
    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)


class GreenUpdateView(UpdateView):
    model = Green
    form_class = ProductForm

    extra_context = {
        'action': 'Изменить'
    }
    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class GreenDeleteView(DeleteView):
    model = Green
    success_url = reverse_lazy('product_list')

    @method_decorator(staff_member_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class GreenDetailView(DetailView):
    model = Green
    extra_context = {
        'form_basket': BasketAddProductForm
    }


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

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

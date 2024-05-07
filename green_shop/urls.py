from django.urls import path
from .views import *

urlpatterns = [
    path('', GreenListView.as_view(), name='product_list'),
    path('products/create/', GreenCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', GreenUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', GreenDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/', GreenDetailView.as_view(), name='product_detail'),
    path('orders/', OrderListView.as_view(), name='order_list'),
]
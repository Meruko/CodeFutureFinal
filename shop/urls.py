from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('orders/', OrderListView.as_view(), name='order_list'),
]

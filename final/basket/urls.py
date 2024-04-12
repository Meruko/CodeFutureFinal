from django.urls import path
from .views import *

urlpatterns = [
    path('', basket_detail, name='basket'),
    path(r'add/<int:product_id>/', basket_add, name='basket_add'),
    path(r'remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path(r'clear/', basket_clear, name='basket_clear'),
    path(r'buy/', basket_buy, name='basket_buy')
]
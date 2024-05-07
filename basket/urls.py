from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_detail, name='basket'),
    path('add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('remove/<int:product_id>/', views.basket_remove, name='basket_remove'),
    path('clear/', views.basket_clear, name='basket_clear'),
    path('buy/', views.basket_buy, name='basket_buy'),
]

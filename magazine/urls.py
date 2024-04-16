from django.urls import path, include
from . import views

urlpatterns_tags = [
    path('', views.template_tags_django, name='template_tags')
]

urlpatterns = [
    path('tags/', include(urlpatterns_tags)),

    path('orders/', views.OrderList.as_view() , name='order_list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreate.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', views.OrderDelete.as_view(), name='order_delete'),

    path('product/', views.ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail')
]

from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'api/supplier', views.SupplierViewSet, basename='supplier')
router.register(r'api/supply', views.SupplyViewSet, basename='supply')
router.register(r'api/product', views.ProductViewSet, basename='product')

urlpatterns += router.urls
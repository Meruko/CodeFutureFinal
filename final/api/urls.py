from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [

]

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'parameter', ParameterViewSet, basename='parameter')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns += router.urls


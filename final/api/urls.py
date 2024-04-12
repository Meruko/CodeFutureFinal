from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [

]

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'parameter', ParameterViewSet, basename='parameter')
router.register(r'pos_parameter', Pos_parameterViewSet, basename='pos_parameter')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'pos_order', Pos_orderViewSet, basename='pos_order')

urlpatterns += router.urls


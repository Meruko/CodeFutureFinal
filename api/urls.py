from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    
]

router = routers.SimpleRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'parameter', views.ParameterViewSet, basename='parameter')
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'pos_parameter', views.Pos_parameterViewSet, basename='pos_parameter')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'pos_order', views.Pos_orderViewSet, basename='pos_order')

urlpatterns += router.urls

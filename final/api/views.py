from rest_framework import viewsets
from .serializers import *


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ParameterViewSet(viewsets.ModelViewSet):
    serializer_class = ParameterSerializer
    queryset = Parameter.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
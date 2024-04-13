from shop.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = [
            'name',
        ]


class ProductSerializer(serializers.ModelSerializer):
    parameters = ParameterSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'date_create',
            'date_update',
            'photo',
            'exists',
            'category',
            'parameters'
        ]


class Pos_parameterSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    parameter = ParameterSerializer(read_only=True)

    class Meta:
        model = Pos_parameter
        fields = [
            'product',
            'parameter',
            'value'
        ]

class ProductOrderSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'category',
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    products = ProductOrderSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'customer',
            'date_create',
            'date_finish',
            'products'
        ]


class Pos_orderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Pos_order
        fields = [
            'product',
            'order',
            'count'
        ]

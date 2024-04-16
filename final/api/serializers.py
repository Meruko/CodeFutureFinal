from shop.models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'pk',
            'name',
            'description'
        ]

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = [
            'pk',
            'name'
        ]

class ProductSerializer(serializers.ModelSerializer):
    parameters = ParameterSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'pk',
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
    class Meta:
        model = Pos_parameter
        fields = [
            'pk',
            'product',
            'parameter',
            'value'
        ]

class ProductOrderSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'price',
            'category'
        ]

class OrderSerializer(serializers.ModelSerializer):
    products = ProductOrderSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = [
            'pk',
            'customer',
            'date_create',
            'date_finish',
            'price',
            'products'
        ]

class Pos_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'pk',
            'product',
            'order',
            'count'
        ]

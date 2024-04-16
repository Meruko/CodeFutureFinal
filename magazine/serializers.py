from rest_framework import serializers
from .models import Supplier, Supply, Pos_supply, Product, Category, Tag, Parametr

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 'description'
        ]

class TagProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name', 'description'
        ]

class ParametrProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametr
        fields = [
            'name'
        ]

class ProductSerializer(serializers.ModelSerializer):
    category = CategoryProductSerializer(read_only=True)
    tag = TagProductSerializer(read_only=True, many=True)
    parametr = ParametrProductSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'price', 'create_date', 'update_date', 'photo', 'exists',
            'category', 'tag', 'parametr'
        ]

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'agent_firstname',
            'agent_name',
            'agent_patronymic',
            'agent_telephone'
        ]

class ProductSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'price'
        ]

class Pos_supplySerializer(serializers.ModelSerializer):
    product = ProductSupplySerializer(read_only=True)
    class Meta:
        model = Pos_supply
        fields = [
            'product',
            'count',
            'price_pos_supply'
        ]

class SupplySerializer(serializers.ModelSerializer):
    supplier = serializers.ChoiceField(choices=Supplier.objects.all(), write_only=True, label='Поставщик')
    pos_supply_set = Pos_supplySerializer(read_only=True, many=True)
    class Meta:
        model = Supply
        fields = [
            'pk',
            'data_supply',
            'supplier',
            'pos_supply_set'
            # 'product'
        ]
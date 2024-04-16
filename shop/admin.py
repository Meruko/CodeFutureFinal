from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
    list_display_links = ('pk', 'name')
    search_fields = ('name', )
    list_editable = ('description', )
    ordering = ('name', )

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')
    search_fields = ('name', )
    ordering = ('name', )

@admin.register(Pos_parameter)
class Pos_parameterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'parameter', 'value')
    list_display_links = ('pk', )
    search_fields = ('product', 'parameter')
    list_editable = ('value', )
    list_filter = ('product', 'parameter')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price', 'exists', 'date_create')
    list_display_links = ('pk', 'name')
    search_fields = ('name', 'price')
    list_editable = ('exists', )
    list_filter = ('exists', 'category')
    ordering = ('date_create', 'name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'customer', 'date_create')
    list_display_links = ('pk', )
    search_fields = ('customer', )
    list_editable = ('customer', )
    ordering = ('date_create', 'date_finish')

@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'order', 'count')
    list_display_links = ('pk',)
    search_fields = ('product', 'order')
    list_editable = ('count', )
    list_filter = ('product', 'order')
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

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
    list_display_links = ('pk', 'name')
    search_fields = ('name', )
    list_editable = ('description', )
    ordering = ('name', )

@admin.register(Pos_type)
class Pos_typeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'green', 'type', 'value')
    list_display_links = ('pk', )
    search_fields = ('green', 'type')
    list_editable = ('value', )
    list_filter = ('green', 'type')

@admin.register(Green)
class GreenAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price', 'exists', 'date_create')
    list_display_links = ('pk', 'name')
    search_fields = ('name', 'price')
    list_editable = ('exists', )
    list_filter = ('category', 'exists')
    ordering = ('date_create', 'name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'customer', 'price', 'date_create')
    list_display_links = ('pk', )
    search_fields = ('customer', )
    list_editable = ('customer', )
    list_filter = ('customer', )
    ordering = ('date_create', 'date_finish')

@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'green', 'order', 'count')
    list_display_links = ('pk', )
    search_fields = ('green', 'order')
    list_editable = ('count', )
    list_filter = ('green', 'order')

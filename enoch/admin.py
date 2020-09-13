from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']
    list_filter = ['price']
    ordering = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'email']
    list_display = ['name', 'phone', 'email', 'total_price']
    list_filter = ['phone', 'email', 'total_price']
    ordering = ['name', 'phone', 'email']

# class CourseResourceInline(admin.TabularInline): # don't this class
#     model = CourseResource
#     extra = 1

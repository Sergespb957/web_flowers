from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # Параметры для отображения в админке
    search_fields = ('name',)  # Поиск по имени продукта

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'date_ordered')  # Параметры для отображения в админке
    list_filter = ('status',)  # Фильтрация по статусу
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .models import Category, Product, Unit


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('product_name', 'product_code', 'product_model','price', 'supplier_price', 'unit', 'category', 'supplier')
    list_filter = ('category', 'unit')
    search_fields = ('name', 'category__name', 'unit__name')


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Unit)
class UnitAdmin(ImportExportModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)

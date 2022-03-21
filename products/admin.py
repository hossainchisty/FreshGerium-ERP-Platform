from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, Unit


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = (
        'product_name',
        'product_code',
        'price',
        'supplier_price',
        'unit',
        'category',
        'in_stock',
        '_status',
        'supplier'

    )
    list_filter = ('status', 'category', 'unit', 'status', 'supplier')
    search_fields = ('name', 'category__name', 'unit__name')
    list_per_page = 20

    fieldsets = (
        (None, {
            "fields": (
                'product_name', 'brand_name', 'manufacturer', 'product_description', 'image', 'in_stock', 'country',
            ),
        }),
        ('Price', {
            'fields': ('price', 'supplier_price')
        }),
        ('Unit', {
            'fields': ('unit',)
        }),
        ('Category', {
            "fields": ('category',),
        }),
        ('Mfg. Date', {
            "fields": ('mfg_date',),
        }),
        ('Exp. Date', {
            "fields": ('exp_date',),
        }),
        ('Barcode and QR Code', {
            'classes': ('collapse',),
            'fields': ('barcode', 'qrcode')
        }),
        ('Supplier', {
            "fields": ('supplier',),
        }),
        ('Other Details', {
            'classes': ('collapse',),
            'fields': (
                'size', 'color', 'weight', 'height', 'shape', 'material_type',
                'hard_disk_size', 'screen_size', 'operating_system', 'cpu_manufacturer',
                'connectivity_technology', 'uses_for_product')
        }),



    )

    def _status(self, obj):
        '''
        This method is used to display the status of the product status in colord text.
        '''
        if obj.out_of_stock is False:
            return format_html('<span style="color: #008000; font-weight: bold;">In Stock</span>')
        elif obj.out_of_stock is True:
            return format_html('<span style="color:#DC143C; font-weight: bold;">Out Of Stock</span>')
        else:
            return obj.status


@ admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    list_per_page = 10


@ admin.register(Unit)
class UnitAdmin(ImportExportModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    list_per_page = 10

from django.contrib import admin
from django.utils.html import format_html
from sales.models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        '_invoice_number', 'customer', 'product',
        'date', 'payment_method', '_status', 'is_paid',
        'total', 'due', 'total_profit',
    )
    list_filter = ('status', 'date', 'payment_method',  'product', 'customer',)
    exclude = ('user', 'status', 'invoice_number')

    def _status(self, obj):
        '''
        Return the status of the sale colorized in red or green depending on the status.
        '''
        return format_html('<span style="color:green">✅Paid</span>') if obj.is_paid else format_html('<span style="color:red">⌛Due</span>')

    def _invoice_number(self, obj):
        '''
        Return the invoice_number colorized in admin.
        '''
        return format_html('<span style="color:green;">#{}</span>', obj.invoice_number)

    def save_model(self, request, obj, form, change):
        '''
        Associate model with current user while saving.
        '''
        obj.user = request.user
        super().save_model(request, obj, form, change)

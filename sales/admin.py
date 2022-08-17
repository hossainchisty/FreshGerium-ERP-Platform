import json
from decimal import Decimal

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.utils.html import format_html
from sales.models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        '_invoice_number', 'customer', 'product',
        'date', 'payment_method', '_status', 'is_paid',
        'due', 'total'
    )
    actions = ('discount_30',)
    list_filter = ('status', 'date', 'payment_method',  'product', 'customer',)
    exclude = ('user', 'status', 'invoice_number')

    def discount_30(self, request, queryset):
        from math import ceil
        discount = 30  # percentage

        for sale in queryset:
            ''' Set a discount of 30% to selected sales '''
            multiplier = discount / 100
            old_price = sale.total
            discounted_price = ceil(old_price - (old_price * Decimal(multiplier)))
            sale.total = discounted_price
            sale.save(update_fields=['total'])
    discount_30.short_description = 'Set 30%% discount'

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

    # def changelist_view(self, request, extra_context=None):
    #     ''' Aggregate new customers per day '''
    #     chart_data = (
    #         Sale.objects.annotate(date=TruncDay("created_at")).values("date")
    #         .annotate(y=Count("id"))
    #         .order_by("-date")
    #     )
    #     # Serialize and attach the chart data to the template context
    #     as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)

    #     extra_context = extra_context or {"chart_data": as_json}

    #     # Call the superclass changelist_view to render the page
    #     return super().changelist_view(request, extra_context=extra_context)

import json

from num2words import num2words

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.utils.html import format_html

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('customer_name', 'gender', 'customer_email', 'mobile_no', 'customer_address', 'city', 'total')
    list_filter = ('gender', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('customer_name', 'gender', 'customer_address', 'city', 'mobile_no', 'customer_email')
        }),

        ('Payment options', {
            'classes': ('collapse',),
            'fields': ('balance', 'previous_balance')
        })
    )

    list_per_page = 10

    @admin.display(empty_value='Not Available')
    def total(self, obj):
        result = obj.balance + obj.previous_balance
        return format_html("<b>{}</b> <br> {}", result, num2words(result).capitalize())

    def changelist_view(self, request, extra_context=None):
        ''' Aggregate new customers per day '''
        chart_data = (
            Customer.objects.annotate(date=TruncDay("created_at")).values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)

        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        '''
        Associate model with current user while saving.
        '''
        obj.user = request.user
        super().save_model(request, obj, form, change)

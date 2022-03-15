from num2words import num2words

from django.contrib import admin
from django.utils.html import format_html

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('customer_name', 'gender', 'customer_email', 'mobile_no', 'customer_address', 'city', 'previous_balance', 'total')
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

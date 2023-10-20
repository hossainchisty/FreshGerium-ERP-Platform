from import_export.admin import ImportExportModelAdmin

from order.models import Order
from django.contrib import admin


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('customer', 'order_date', 'status', 'total_amount')

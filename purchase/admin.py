from django.contrib import admin

from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'purchase_date'
    list_display = (
        'product', 'supplier', 'invoice_number',
        'purchase_id', 'purchase_date', 'payment_method',
        'discount', 'paid_amount', 'due_amount', 'total_amount'
    )
    list_filter = ('purchase_date', 'payment_method')
    fieldsets = (
        (None, {
            'fields': ('user', 'product', 'supplier', 'purchase_date', 'payment_method', 'details',
                       'discount', 'paid_amount', 'due_amount', 'total_amount')
        }),
    )
    readonly_fields = ('invoice_number', 'purchase_id',)
    search_fields = ('invoice_number', 'purchase_id',)
    ordering = ('-purchase_date',)
    list_per_page = 10
    exclude = ('invoice_number', 'purchase_id',)
    list_editable = ('paid_amount', 'due_amount',)

    def save_model(self, request, obj, form, change):
        '''
        Associate model with current user while saving.
        '''
        obj.user = request.user
        super().save_model(request, obj, form, change)

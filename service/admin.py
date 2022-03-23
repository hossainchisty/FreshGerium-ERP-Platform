from django.contrib import admin
from service.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service_name', 'description', 'charge')
    search_fields = ('service_name',)
    list_filter = ('customer',)
    ordering = ('customer',)

    def save_model(self, request, obj, form, change):
        '''
        Associate model with current user while saving.
        '''
        obj.user = request.user
        super().save_model(request, obj, form, change)

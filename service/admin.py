from django.contrib import admin
from service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service_name', 'description', 'charge')
    search_fields = ('service_name',)
    list_filter = ('customer',)
    ordering = ('customer',)
    
admin.site.register(Service, ServiceAdmin)

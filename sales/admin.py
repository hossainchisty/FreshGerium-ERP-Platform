from django.contrib import admin

from .models import Sale

admin.site.register(Sale)
admin.site.site_header = 'Freshdesk CRM Platform'

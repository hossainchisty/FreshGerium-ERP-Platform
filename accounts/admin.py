from django.contrib import admin
from .models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name','account_description','country')


admin.site.register(Account, AccountAdmin)
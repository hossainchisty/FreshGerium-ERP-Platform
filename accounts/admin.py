from accounts.models.account_models import Account
from accounts.models.bank_account_model import Bank
from django.contrib import admin


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_account_name', 'bank_account_number', 'account_type', 'bank_name', 'bank_short_name', 'bank_branch')
    search_fields = ('bank_account_name', 'bank_account_number')
    list_filter = ('account_type', 'bank_name', 'bank_short_name', 'bank_branch')
    list_per_page = 10
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        '''
        Associate model with current user while saving.
        '''
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country', 'industry')
    list_filter = ('industry',)

from accounts.views.account_views import AccountView
from accounts.views.bank_account_list import BankAccountList
from django.urls import include, path

urlpatterns = [
    path('', AccountView.as_view(), name='accounts'),
    path('bank/accounts/', BankAccountList.as_view(), name='bank_accounts'),
    path('api/v1/', include('accounts.api.urls.accounts_urls')),
]

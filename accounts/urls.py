from accounts.views.account_views import AccountView
from accounts.views.bank_account_details import BankAccountDetails
from accounts.views.bank_account_list import BankAccountList
from django.urls import include, path

urlpatterns = [
    path('', AccountView.as_view(), name='accounts'),
    path('view/<pk>/', BankAccountDetails.as_view(), name='bank_account_details'),
    path('bank/accounts/', BankAccountList.as_view(), name='bank_accounts'),
    path('api/v1/', include('accounts.api.urls.accounts_urls')),
]

from accounts.views.account_views import accounts
from django.urls import include, path

urlpatterns = [
    path('', accounts, name='accounts'),
    path('api/v1/', include('accounts.api.urls.accounts_urls')),
]

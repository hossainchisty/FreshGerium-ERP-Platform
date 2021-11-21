from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('accounts.api.urls.accounts_urls')),
]

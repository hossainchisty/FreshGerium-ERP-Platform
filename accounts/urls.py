from django.urls import path, include

urlpatterns = [
    path('api/', include('accounts.api.urls.accounts_urls')),
]

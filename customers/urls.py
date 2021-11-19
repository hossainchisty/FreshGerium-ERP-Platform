
from django.urls import include, path

urlpatterns = [
    path('api/', include('customers.api.urls.customer_urls')),
]

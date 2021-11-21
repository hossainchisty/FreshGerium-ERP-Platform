
from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('customers.api.urls.customer_urls')),
]

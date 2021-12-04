
from customers.views.customer_views import Customer
from django.urls import include, path

urlpatterns = [
    path('', Customer.as_view(), name='customer'),
    path('api/v1/', include('customers.api.urls.customer_urls')),
]

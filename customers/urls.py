
from customers.views.customer_views import customer
from django.urls import include, path

urlpatterns = [
    path('', customer, name='customer'),
    path('api/v1/', include('customers.api.urls.customer_urls')),
]

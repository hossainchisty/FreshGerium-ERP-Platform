
from customers.views.create_customer_views import CreateCustomer
from customers.views.customer_views import CustomerList
from django.urls import include, path

urlpatterns = [
    path('', CustomerList.as_view(), name='customer_list'),
    path('add/', CreateCustomer.as_view(), name='add_customer'),
    path('api/v1/', include('customers.api.urls.customer_urls')),
]

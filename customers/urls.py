
from customers.views.customer_views import CustomerList
from django.urls import include, path

urlpatterns = [
    path('', CustomerList.as_view(), name='customer_list'),
    path('api/v1/', include('customers.api.urls.customer_urls')),
]

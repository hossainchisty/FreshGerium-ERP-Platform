
from customers.views.create_customer_views import CreateCustomer
from customers.views.customer_views import CustomerLedgerList, CustomerList
from customers.views.delete_customer_views import DeleteCustomer
from customers.views.update_customer_views import UpdateCustomer
from django.urls import include, path

urlpatterns = [
    path('list/', CustomerList.as_view(), name='customer_list'),
    path('ledger/', CustomerLedgerList.as_view(), name='customer_ledger_list'),

    path('add/', CreateCustomer.as_view(), name='add_customer'),
    path('update/<int:pk>/', UpdateCustomer.as_view(), name='update_customer'),
    path('delete/<pk>', DeleteCustomer.as_view(), name='delete_customer'),

    # API URLs
    # path('api/v1/', include('customers.api.urls.customer_urls')),
]

from customers.models import Customer
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class DeleteCustomer(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')

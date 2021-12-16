from customers.models import Customer
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class UpdateCustomer(UpdateView):
    model = Customer
    fields = ['customer_name', 'customer_email', 'customer_address', 'mobile_no', 'balance', 'previous_balance']
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customer_list')

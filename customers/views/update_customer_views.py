from customers.models import Customer
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class UpdateCustomer(UpdateView):
    model = Customer
    fields = ['customer_name', 'customer_email', 'customer_address', 'mobile_no', 'balance', 'previous_balance']
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customer_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this customer.")
        return obj

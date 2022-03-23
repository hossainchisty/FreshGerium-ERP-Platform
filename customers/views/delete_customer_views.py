from customers.models import Customer
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.core.exceptions import PermissionDenied


class DeleteCustomer(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this customer.")
        return obj

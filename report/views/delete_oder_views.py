from order.models import Order
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class DeleteOrder(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this order.")
        return obj

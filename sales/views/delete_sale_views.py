from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from sales.models import Sale


class DeleteSale(DeleteView):
    model = Sale
    success_url = reverse_lazy('sales_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this sale.")
        return obj

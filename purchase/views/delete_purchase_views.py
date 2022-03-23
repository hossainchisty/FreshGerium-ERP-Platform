from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from purchase.models import Purchase


class DeletePurchase(DeleteView):
    model = Purchase
    success_url = reverse_lazy('manage_purchase')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this purchase.")
        return obj

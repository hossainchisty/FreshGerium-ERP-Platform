from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from purchase.models import Purchase


class UpdatePurchase(UpdateView):
    model = Purchase
    fields = ['purchase_date', 'total_amount', 'supplier']
    template_name = 'purchase/purchase_form.html'
    success_url = reverse_lazy('manage_purchase')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this purchase.")
        return obj

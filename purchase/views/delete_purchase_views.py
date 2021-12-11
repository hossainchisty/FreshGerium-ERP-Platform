from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from purchase.models import Purchase


class DeletePurchase(DeleteView):
    model = Purchase
    success_url = reverse_lazy('manage_purchase')

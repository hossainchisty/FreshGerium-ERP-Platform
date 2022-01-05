from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from sales.models import Sale


class DeleteSale(DeleteView):
    model = Sale
    success_url = reverse_lazy('sales_list')

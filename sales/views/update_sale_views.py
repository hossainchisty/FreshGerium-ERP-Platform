from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from sales.models import Sale


class UpdateSale(UpdateView):
    model = Sale
    fields = '__all__'
    template_name = 'sales/sales_form.html'
    success_url = reverse_lazy('sales_list')

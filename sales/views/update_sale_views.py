from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from sales.models import Sale


class UpdateSale(UpdateView):
    ''' This view is used to update the sale model. '''
    model = Sale
    fields = ['invoice_number', 'customer', 'product', 'date', 'payment_method', 'is_paid', 'discount', 'due', 'total']
    template_name = 'sales/sales_form.html'
    success_url = reverse_lazy('sales_list')

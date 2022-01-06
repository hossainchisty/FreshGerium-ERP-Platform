import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from purchase.models import Purchase
from utils.helper.decorators.filter import _currentUser


class DownloadPurchaseCSV(LoginRequiredMixin, View):
    '''
    Automaticly download purchase data as CSV file.
    '''
    @method_decorator(_currentUser())
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        write = csv.writer(response)
        write.writerow(["Invoice Number", "Purchase Id", "Purchase Date", "Total Amount", "Supplier"])
        for purchase in Purchase.objects.all():
            write.writerow([purchase.invoice_number, purchase.purchase_id, purchase.purchase_date, purchase.total_amount, purchase.supplier])
            response["Content-Disposition"] = "attachment; filename=purchase-data.csv"
            return response

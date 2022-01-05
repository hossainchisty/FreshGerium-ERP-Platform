import csv

from django.http import HttpResponse
from django.views.generic import View
from sales.models import Sale


class DownloadSaleCSV(View):
    '''
    Automaticly download sales data as CSV file.
    '''
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        write = csv.writer(response)
        write.writerow(["Invoice Number", "Customer", "Product", "Date", "Discount", "Payment Method", "Status", "Total Profit", "Due", "Total"])
        for sale in Sale.objects.all():
            write.writerow([sale.invoice_number, sale.customer, sale.product, sale.date, sale.discount, sale.payment_method, sale.status, sale.total_profit, sale.due, sale.total])
            response["Content-Disposition"] = "attachment; filename=sales-data.csv"
            return response

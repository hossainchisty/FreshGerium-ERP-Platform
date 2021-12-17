import csv

from django.http import HttpResponse
from django.views.generic import View
from stock.models import Stock


class DownloadStockCSV(View):
    '''
    Automaticly download stock data as CSV file.
    '''
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        write = csv.writer(response)
        write.writerow(["Product Name", "Product Model", "Sale Price", "Purchase Price", "In Qnty", "Out Qnty", "Total Stock", "Stock Sale Price"])
        for stock in Stock.objects.all():
            write.writerow([stock.product.product_name, stock.product.product_model, stock.sale_price, stock.purchase_price, stock.in_qnty, stock.out_qnty, stock.stock, stock.sale_price])
            response["Content-Disposition"] = "attachment; filename=stock-data.csv"
            return response

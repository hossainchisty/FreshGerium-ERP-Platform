import datetime

import xlwt

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from stock.models import Stock
from utils.helper.decorators.filter import _currentUser


class DownloadStockExcel(LoginRequiredMixin, View):
    '''
    Automaticly download stock data as Excle file.
    '''
    @method_decorator(_currentUser())
    def get(self, request):
        # content-type of response
        response = HttpResponse(content_type="application/ms-excel")

        # decide file name
        response['Content-Disposition'] = 'attachment; filename="Stock"{}.xlsx"'.format(datetime.datetime.now().strftime("%Y-%m-%d"))

        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet('Stock')

        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # headers are of center alignment
        font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER

        # column header name.
        columns = ["Product Name", "Product Model", "Sale Price", "Purchase Price", "In Qnty", "Out Qnty", "In Stock", "Sale Price"]

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        # Sheet body center alignment
        font_style.alignment.horz = xlwt.Alignment.VERT_CENTER

        # Get all stock data
        rows = Stock.objects.all().values_list('product.product_name', 'product.product_model', 'sale_price', 'purchase_price', 'in_qnty', 'out_qnty', 'stock', 'sale_price')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
        wb.save(response)
        return response

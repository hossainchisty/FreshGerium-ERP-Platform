import datetime

import xlwt

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View
from purchase.models import Purchase


class DownloadPurchaseEXCLE(LoginRequiredMixin, View):
    '''
    Automaticly download purchase data as Excle file.
    '''
    def get(self, request):
        # content-type of response
        response = HttpResponse(content_type="application/ms-excel")

        # decide file name
        response['Content-Disposition'] = 'attachment; filename="Purchase"{}.xlsx"'.format(datetime.datetime.now().strftime("%Y-%m-%d"))

        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet('Purchase')

        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # column header name.
        columns = ['Invoice Number', 'Purchase Id', 'Purchase Date', 'Total Amount', 'Supplier']

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        # Get all purchase data
        rows = Purchase.objects.all().values_list('invoice_number', 'purchase_id', 'purchase_date', 'total_amount', 'supplier')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
        wb.save(response)
        return response

import datetime

import xlwt

from damage.models import Damage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View


class DownloadDamageEXCLE(LoginRequiredMixin, View):
    '''
    Automaticly download service data as Excle file.
    '''
    def get(self, request):
        # content-type of response
        response = HttpResponse(content_type="application/ms-excel")

        # decide file name
        response['Content-Disposition'] = 'attachment; filename="Damage"{}.xlsx"'.format(datetime.datetime.now().strftime("%Y-%m-%d"))

        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet('Damage')

        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # headers are of center alignment
        font_style.alignment.horz = xlwt.Alignment.HORZ_CENTER

        # column header name.
        columns = ["Product", "Customer", "Supplier", "Damaged Date", "Damaged Reason", "Note"]

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        # Sheet body center alignment
        font_style.alignment.horz = xlwt.Alignment.VERT_CENTER

        # Get all damage data
        rows = Damage.objects.all().values_list('product', 'customer', 'supplier', 'damaged_date', 'damaged_reason', 'note')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
        wb.save(response)
        return response

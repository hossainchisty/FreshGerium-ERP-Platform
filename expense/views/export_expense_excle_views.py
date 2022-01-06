import datetime

import xlwt

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from expense.models import Expense
from utils.helper.decorators.filter import _currentUser


class DownloadExpenseEXCLE(LoginRequiredMixin, View):
    '''
    Automaticly download expense data as Excle file.
    '''
    @method_decorator(_currentUser())
    def get(self, request):
        # content-type of response
        response = HttpResponse(content_type="application/ms-excel")

        # decide file name
        response['Content-Disposition'] = 'attachment; filename="Expense"{}.xlsx"'.format(datetime.datetime.now().strftime("%Y-%m-%d"))

        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet('Expense')

        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # column header name.
        columns = ['Date', 'Expense Type', 'Amount']

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        # Get all expense data
        rows = Expense.objects.all().values_list('date', 'expense_type', 'amount')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
        wb.save(response)
        return response

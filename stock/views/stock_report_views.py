from django.shortcuts import render
from django.views.generic import View


class StockReportView(View):
    def get(self, request):
        '''
        TODO:
         - List of stock report
         - Generate report CSV, PDF, PRINT, EXCEL
        '''
        return render(request, 'stock/stock_report.html')

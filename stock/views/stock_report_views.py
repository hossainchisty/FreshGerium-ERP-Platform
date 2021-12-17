from django.shortcuts import render
from django.views.generic import View
from stock.models import Stock


class StockReportView(View):
    def get(self, request):
        '''List of stock reports'''
        stocks = Stock.objects.all()

        context = {
            'stocks': stocks
        }
        return render(request, 'stock/stock_report.html', context)

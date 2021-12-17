from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from stock.models import Stock


class StockReportView(View):
    def get(self, request):
        '''List of stock reports'''
        stock_list = Stock.objects.all()
        paginator = Paginator(stock_list, 25) # Show 25 customers per page.
        page_number = request.GET.get('page')
        stocks = paginator.get_page(page_number)


        context = {
            'stocks': stocks
        }
        return render(request, 'stock/stock_report.html', context)

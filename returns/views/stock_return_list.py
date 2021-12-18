from django.shortcuts import render
from django.views.generic import View


class StockReturnView(View):
    def get(self, request):
        return render(request, 'return/stock_return.html')

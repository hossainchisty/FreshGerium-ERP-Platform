from django.shortcuts import render
from django.views.generic import View


class SalesList(View):
    def get(self, request):
        '''
        TODO:
        - This will reutrn list of sales
        '''
        return render(request, 'sales/sales_list.html')

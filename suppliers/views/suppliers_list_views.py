from django.shortcuts import render
from django.views.generic import View


class SupplierList(View):
    def get(self, request):
        '''
        TODO:
        - This will reutrn list of suppliers
        '''
        return render(request, 'suppliers/suppliers_list.html')

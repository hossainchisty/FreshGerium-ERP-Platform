from django.shortcuts import render
from django.views.generic import View


class SuppliersLedgerList(View):
    def get(self, request):
        '''
        TODO:
        - This will reutrn suppliers ledger list
        '''
        return render(request, 'suppliers/suppliers_ledger_list.html')

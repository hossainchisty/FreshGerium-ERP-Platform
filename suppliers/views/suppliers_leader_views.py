from django.shortcuts import render
from django.views.generic import View
from suppliers.models import Supplier
from utils.models.common_fields import Ledger


class SuppliersLedgerList(View):
    def get(self, request):
        ''' This will reutrn suppliers ledger list '''
        supplier = Supplier.objects.all().order_by('-id')
        supplier_ledger = Supplier.objects.prefetch_related('supplier_ledger')

        context = {
            'suppliers': supplier_ledger,
            'supplier_ledgers': supplier_ledger
        }
        return render(request, 'suppliers/suppliers_ledger_list.html', context)

from django.shortcuts import render
from django.views.generic import View
from suppliers.models import Supplier


class SupplierList(View):
    def get(self, request):
        '''List of suppliers'''
        suppliers = Supplier.objects.all()

        context = {
            'suppliers': suppliers
        }
        return render(request, 'suppliers/suppliers_list.html', context)

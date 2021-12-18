from django.shortcuts import render
from django.views.generic import View


class SupplierReturnView(View):
    def get(self, request):
        return render(request, 'return/supplier_return.html')

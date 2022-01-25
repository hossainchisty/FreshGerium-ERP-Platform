from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from suppliers.models import Supplier


class SupplierList(View):
    def get(self, request):
        '''List of suppliers'''
        supplier_list = Supplier.objects.all().order_by('-id')
        paginator = Paginator(supplier_list, 25)
        page_number = request.GET.get('page')
        suppliers = paginator.get_page(page_number)

        context = {
            'suppliers': suppliers
        }
        return render(request, 'suppliers/suppliers_list.html', context)

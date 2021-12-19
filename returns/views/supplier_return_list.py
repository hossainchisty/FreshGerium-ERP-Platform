from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from returns.models import Return


class SupplierReturnView(View):
    def get(self, request):
        '''
        This will reutrn list of supplier return items
        '''
        return_list = Return.objects.all()
        paginator = Paginator(return_list, 10)
        page_number = request.GET.get('page')
        returns = paginator.get_page(page_number)

        context = {
            'supplier_return': returns,
        }
        return render(request, 'return/supplier_return.html', context)

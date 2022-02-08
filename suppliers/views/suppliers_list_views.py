from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from utils.helper.decorators.filter import _currentUser
from django.views.generic import View
from suppliers.models import Supplier


@method_decorator(cache_page(60 * 5), name='dispatch')
class SupplierList(View):

    @method_decorator(_currentUser())
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

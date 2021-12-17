from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from sales.models import Sale


class SalesList(View):
    def get(self, request):
        ''' List of all sales '''
        sales_list = Sale.objects.all().order_by('-id')
        paginator = Paginator(sales_list, 25)
        page_number = request.GET.get('page')
        sales = paginator.get_page(page_number)

        context = {
            'sales': sales
        }
        return render(request, 'sales/sales_list.html', context)

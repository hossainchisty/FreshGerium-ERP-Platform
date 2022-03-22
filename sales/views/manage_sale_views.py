from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View
from sales.models import Sale


@method_decorator(cache_page(60 * 2), name='dispatch')
class SalesList(View):
    def get(self, request):
        ''' List of all sales '''
        sales_list = Sale.objects.all().order_by('-id')
        paginator = Paginator(sales_list, 10)
        page_number = request.GET.get('page')

        try:
            page_object = paginator.page(page_number)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_object = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_object = paginator.page(paginator.num_pages)

        context = {
            'sales': page_object
        }
        return render(request, 'sales/sales_list.html', context)

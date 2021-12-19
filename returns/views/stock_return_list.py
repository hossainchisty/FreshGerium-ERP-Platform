from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from returns.models import Return


class StockReturnView(View):
    def get(self, request):
        '''
        This will reutrn list of stock return items
        '''
        return_list = Return.objects.all()
        paginator = Paginator(return_list, 20)
        page_number = request.GET.get('page')
        returns = paginator.get_page(page_number)

        context = {
            'returns': returns,
        }
        return render(request, 'return/stock_return.html', context)

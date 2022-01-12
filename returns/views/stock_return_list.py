from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from returns.models import Return
from utils.helper.decorators.filter import _currentUser


class StockReturnView(LoginRequiredMixin, View):

    @method_decorator(_currentUser())
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

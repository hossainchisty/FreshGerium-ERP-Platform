from order.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.helper.decorators.filter import _currentUser


class OrderList(LoginRequiredMixin, View):

    @method_decorator(_currentUser())
    def get(self, request):
        '''
        This will reutrn list of order items
        '''
        order_list = Order.objects.all().order_by('-id')
        paginator = Paginator(order_list, 25)
        page_number = request.GET.get('page')
        order = paginator.get_page(page_number)

        context = {
            'orders': order
        }
        return render(request, 'order/manage_order.html', context)

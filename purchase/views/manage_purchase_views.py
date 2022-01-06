from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from purchase.models import Purchase
from utils.helper.decorators.filter import _currentUser


class ManagePurchase(LoginRequiredMixin, View):
    '''
    List of all purchases
    '''
    @method_decorator(_currentUser())
    def get(self, request):
        purchase_list = Purchase.objects.all().order_by('-id')
        paginator = Paginator(purchase_list, 25) # Show 25 customers per page.
        page_number = request.GET.get('page')
        purchases = paginator.get_page(page_number)

        context = {
            'purchases': purchases
        }
        return render(request, 'purchase/manage_purchase.html', context)

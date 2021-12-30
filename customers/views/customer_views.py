from customers.models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.helper.decorators.filter import currentUser
from utils.models.common_fields import Ledger


class CustomerList(LoginRequiredMixin, View):

    @method_decorator(currentUser())
    def get(self, request):
        '''
        This will reutrn list of customer
        '''
        customer_list = Customer.objects.all().order_by('-id')
        paginator = Paginator(customer_list, 25)
        page_number = request.GET.get('page')
        customers = paginator.get_page(page_number)

        context = {
            'customers': customers
        }
        return render(request, 'customers/customer.html', context)


class CustomerLedgerList(View):

    @method_decorator(currentUser())
    def get(self, request):
        '''
        This will reutrn list of customer ledger
        '''
        customer_balance = Customer.objects.all().order_by('-id')

        customer_ledger = Ledger.objects.all().order_by('-id')

        context = {
            'customer_balance': customer_balance,
            'customer_ledger': customer_ledger
        }
        return render(request, 'customers/customer_ledger.html', context)

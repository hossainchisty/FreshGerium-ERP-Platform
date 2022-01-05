from accounts.models.bank_account_model import Bank
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.helper.decorators.filter import _currentUser


class BankAccountList(LoginRequiredMixin, View):

    @method_decorator(_currentUser())
    def get(self, request, *args, **kwarg):
        ''' This will reutrn list of bank accounts '''
        bank_account_list = Bank.objects.all().order_by('-id')
        paginator = Paginator(bank_account_list, 25)
        page_number = request.GET.get('page')
        bank_account_list = paginator.get_page(page_number)

        context = {
            'bank_account_list': bank_account_list
        }
        return render(request, 'accounts/bank_account_list.html', context)

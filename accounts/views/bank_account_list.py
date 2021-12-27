from accounts.models.bank_account_model import Bank
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View


class BankAccountList(View):

    def get(self, request):
        ''' This will reutrn list of bank accounts '''
        bank_account_list = Bank.objects.all().order_by('-id')
        paginator = Paginator(bank_account_list, 25)
        page_number = request.GET.get('page')
        bank_account_list = paginator.get_page(page_number)

        context = {
            'bank_account_list': bank_account_list
        }
        return render(request, 'accounts/bank_account_list.html', context)

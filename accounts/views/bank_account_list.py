from accounts.models.bank_account_model import Bank
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.helper.decorators.filter import _currentUser


class BankAccountList(LoginRequiredMixin, View):

    @method_decorator(_currentUser())
    def get(self, request, *args, **kwarg):
        ''' This will reutrn list of bank accounts '''
        object_list = Bank.objects.all().order_by('-id')

        page_number = request.GET.get('page')
        paginator = Paginator(object_list, 10)
        try:
            page_object = paginator.page(page_number)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_object = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_object = paginator.page(paginator.num_pages)

        context = {
            'bank_account_list': page_object
        }
        return render(request, 'accounts/bank_account_list.html', context)

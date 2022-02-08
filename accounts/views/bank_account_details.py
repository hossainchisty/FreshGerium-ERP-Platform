from accounts.models.bank_account_model import Bank
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.detail import DetailView


@method_decorator(cache_page(60 * 5), name='dispatch')
class BankAccountDetails(DetailView):
    ''' This class will return the bank account details. '''
    model = Bank
    template_name = 'accounts/bank_account_details.html'

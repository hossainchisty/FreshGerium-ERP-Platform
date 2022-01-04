from accounts.models.bank_account_model import Bank
from django.views.generic.detail import DetailView


class BankAccountDetails(DetailView):
    ''' This class will return the bank account details. '''
    model = Bank
    template_name = 'accounts/bank_account_details.html'

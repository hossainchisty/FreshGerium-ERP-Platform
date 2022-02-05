from accounts.models.account_models import Account
from accounts.models.bank_account_model import Bank
from customers.models import Customer
from damage.models import Damage
from django.shortcuts import render
from expense.models import Category, Expense
from purchase.models import Purchase
from service.models import Service


def _currentUser():
    '''
    This decorator for authenticated users only, and filtering by the logged in user from the request, another user, even if logged in, can't access another user's data.
    '''
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            models = Damage
            models = Bank
            models = Account
            models = Expense
            models = Category
            models = Purchase
            models = Service
            models = Customer
            selected_user = models.objects.filter(user=request.user)
            if selected_user:
                return func(request, *args, **kwargs)
            else:
                return render(request, 'core/error/403.html')

        return wrapper
    return decorator

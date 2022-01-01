from accounts.models.account_models import Account
from accounts.models.bank_account_model import Bank
from customers.models import Customer
from django.http import HttpResponseForbidden


def currentUser():
    '''
    This decorator for authenticated users only, and filtering by the logged in user from the request, another user, even if logged in, can't access another user's data.
    '''
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            models = Bank
            models = Customer
            models = Account
            selected_user = models.objects.filter(user=request.user)
            if selected_user:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden('<h1>Access Denied</h1>')

        return wrapper
    return decorator

from django.shortcuts import render
from django.http import HttpResponseForbidden
from accounts.models.account_models import Account
from accounts.models.bank_account_model import Bank
from customers.models import Customer
from returns.models import Return
from report.models import Report
from damage.models import Damage
from expense.models import Category, Expense
from purchase.models import Purchase
from service.models import Service
from order.models import Order

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            allowed_models = [Order, Damage, Bank, Account, Expense, Category, Purchase, Service, Customer, Return, Report]
            for model in allowed_models:
                obj = model.objects.filter(user=request.user, **request.GET.dict()).first()
                if obj:
                    return response

            # No matching object found, return 403 error
            return HttpResponseForbidden(render(request, 'core/error/403.html'))
        # User not authenticated, return 403 error
        return HttpResponseForbidden(render(request, 'core/error/403.html'))

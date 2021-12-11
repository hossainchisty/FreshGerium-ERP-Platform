from datetime import date

from django import template
from django.db.models import Sum
from expense.models import Expense

register = template.Library()


@register.simple_tag
def get_today_expsense():
    '''
    This method is used to get today total expense.
    '''
    if Expense.objects.filter(date=date.today()).exists():
        return Expense.objects.filter(date=date.today()).aggregate(Sum('amount'))['amount__sum']
    else:
        return 0.00

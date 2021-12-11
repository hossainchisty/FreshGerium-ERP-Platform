from datetime import date

from django import template
from django.db.models import Sum
from expense.models import Expense

register = template.Library()


@register.simple_tag
def get_today_expsense(default=0.00):
    '''
    This method is used to get today total expense.
    '''
    return Expense.objects.filter(date=date.today()).aggregate(Sum('amount'))['amount__sum'] or default

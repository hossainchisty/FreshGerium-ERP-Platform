from django import template
from django.db.models import Sum
from expense.models import Expense

register = template.Library()


@register.simple_tag
def get_total_expsense(default=0.00):
    '''
    This method is used to get total expense.
    '''
    return Expense.objects.aggregate(Sum('amount'))['amount__sum'] or default

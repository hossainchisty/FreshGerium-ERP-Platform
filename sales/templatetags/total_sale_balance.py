
from django import template
from django.db.models import Sum
from sales.models import Sale

register = template.Library()


@register.simple_tag
def total_balance(self):
    '''
    This method is used to get total balance.
    '''
    return Sale.objects.aggregate(Sum('paid_amount'))['paid_amount__sum']

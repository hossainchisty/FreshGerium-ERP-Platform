from django import template
from django.db.models import Sum
from sales.models import Sale

register = template.Library()


@register.simple_tag
def get_total_profit(default=0.00):
    ''' Calculate the total profit. '''
    return Sale.objects.aggregate(Sum('total_profit'))['total_profit__sum'] or default

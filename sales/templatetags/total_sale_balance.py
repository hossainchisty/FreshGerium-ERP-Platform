
from django import template
from django.db.models import Sum
from sales.models import Sale

register = template.Library()


@register.simple_tag
def total_balance(default=0.00):
    ''' Calculate sum of total sale balance '''
    return Sale.objects.aggregate(Sum('total'))['total__sum']

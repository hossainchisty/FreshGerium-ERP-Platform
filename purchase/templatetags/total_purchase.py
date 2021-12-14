
from django import template
from django.db.models import Sum
from purchase.models import Purchase

register = template.Library()


@register.simple_tag
def get_total_purchase(defalut=0.00):
    '''
    This method is to calculate the total product cost
    '''
    return Purchase.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or defalut

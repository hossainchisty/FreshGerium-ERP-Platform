from customers.models import Customer
from django import template
from django.db.models import Sum

register = template.Library()


@register.simple_tag
def total_balance():
    '''
    This method is used to get total balance.
    '''
    return Customer.objects.aggregate(Sum('balance'))['balance__sum']


@register.simple_tag
def total_customer():
    '''
    This method is used to get total customer.
    '''
    return Customer.objects.all().count()

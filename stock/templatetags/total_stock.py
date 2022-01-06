from django import template
from stock.models import Stock

register = template.Library()


@register.simple_tag
def get_total_stock(defalut=0):
    ''' Calculate the total stock. '''
    return Stock.objects.all().count() or defalut

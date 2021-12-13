from django import template
from suppliers.models import Supplier

register = template.Library()


@register.simple_tag
def get_total_supplier(defalut=0):
    '''
    This method is used to calculate the total supplier.
    '''
    return Supplier.objects.all().count() or defalut


from django import template
from products.models import Product

register = template.Library()


@register.simple_tag
def get_total_product(defalut=0):
    '''
    This method is to calculate the total product
    '''
    return Product.objects.all().count() or defalut

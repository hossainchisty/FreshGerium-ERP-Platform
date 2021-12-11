
from django import template
from sales.models import Sale

register = template.Library()


@register.simple_tag
def get_total_sale(default=0.00):
    '''
    This method is used to calculate the total sales.
    '''
    return Sale.objects.all().count() or default

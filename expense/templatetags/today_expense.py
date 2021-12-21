from datetime import date

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Sum
from expense.models import Expense

register = template.Library()


@register.simple_tag
def get_today_expsense(default=0.00):
    ''' Calculate the today total expense. '''
    return intcomma(Expense.objects.filter(date=date.today()).aggregate(Sum('amount'))['amount__sum'] or default)

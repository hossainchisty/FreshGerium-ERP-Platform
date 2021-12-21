import datetime

import pytz

from django.db.models import Sum
from expense.models import Expense

current = datetime.datetime.now(pytz.timezone('Asia/Dhaka'))


def get_total_expsense(default=0.00):
    ''' Calculate the total expense of all expense. '''
    total_expsense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or default
    return {'total_expsense': total_expsense}


def get_total_expsense_by_month(default=0.00):
    ''' Calculate the total expense by current month. '''
    expsense_by_month = Expense.objects.filter(date__month=current.month, date__year=current.year).aggregate(Sum('amount'))['amount__sum'] or default
    return {'total_expsense_by_month': expsense_by_month}


def get_total_expsense_by_year(default=0.00):
    ''' Calculate the total expense by current year. '''
    expsense_by_year = Expense.objects.filter(date__year=current.year).aggregate(Sum('amount'))['amount__sum'] or default
    return {'total_expsense_by_year': expsense_by_year}

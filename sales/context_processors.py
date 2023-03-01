# flake8: noqa
import datetime
from datetime import date

from django.db.models import Sum
from sales.models import Sale


def march_sales(default=0.00):
    sales = Sale.objects.all()
    months = sales.datetimes('created_at', kind="month")
    for month in months:
        month_sale = sales.filter(created_at__month=month.month)
        month_total = month_sale.aggregate(Sum('total'))['total__sum'] or default
        print(f'Month: {month.strftime("%B - %m year: %Y")}- {month.month} Total Sale: {month_total}')
        print(month.strftime("%b"))
        return {'month_total': month_total, 'months': month.strftime("%b")}


print(march_sales())


def january_sales(default=0.00):
    january_month = [i.month for i in Sale.objects.values_list('date', flat=True) if i.year == date.today().year and i.month == 1]
    joanuary_month_total = Sale.objects.filter(date__month__in=january_month).aggregate(Sum('total'))['total__sum'] or default
    return {'january_month_total': january_month_total}


def february_sales(default=0.00):
    february_month = [i.month for i in Sale.objects.values_list('date', flat=True) if i.year == date.today().year and i.month == 2]
    february_month_total = Sale.objects.filter(date__month__in=february_month).aggregate(Sum('total'))['total__sum'] or default
    return {'february_month_total': february_month_total}

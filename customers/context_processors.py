import datetime

from customers.models import Customer


def customer_created_at_january(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_january': Customer.objects.filter(created_at__month=1).count() or default}


def customer_created_at_february(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_february': Customer.objects.filter(created_at__month=2).count() or default}


def customer_created_at_march(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_march': Customer.objects.filter(created_at__month=3).count() or default}


def customer_created_at_april(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_april': Customer.objects.filter(created_at__month=4).count() or default}


def customer_created_at_may(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_may': Customer.objects.filter(created_at__month=5).count() or default}


def customer_created_at_june(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_june': Customer.objects.filter(created_at__month=6).count() or default}


def customer_created_at_july(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_july': Customer.objects.filter(created_at__month=7).count() or default}


def customer_created_at_august(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_august': Customer.objects.filter(created_at__month=8).count() or default}


def customer_created_at_september(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_september': Customer.objects.filter(created_at__month=9).count() or default}


def customer_created_at_october(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_october': Customer.objects.filter(created_at__month=10).count() or default}


def customer_created_at_november(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_november': Customer.objects.filter(created_at__month=11).count() or default}


def customer_created_at_december(default=0):
    '''
    Get total number of customers by created month.
    '''
    return {'created_at_december': Customer.objects.filter(created_at__month=12).count() or default}


def customer_created_at_current_year(default=0):
    '''
    Get total number of customers by created year.
    '''
    return {'total_customer_created_by_year': Customer.objects.filter(created_at__year=datetime.datetime.now().year).count() or default}

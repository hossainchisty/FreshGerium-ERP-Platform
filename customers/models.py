from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from utils.models.common_fields import Ledger, Timestamp


class Customer(Timestamp):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    GENDER_SELECT = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=200, choices=GENDER_SELECT)
    customer_address = models.TextField()
    mobile_no = PhoneNumberField(default="+8801")
    city = CountryField(default="BD")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    previous_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    customer_ledger = models.ManyToManyField(Ledger)

    @property
    def total_customer(self):
        '''
        This method is used to get total customer.
        '''
        return Customer.objects.all().count()

    @property
    def total_balance(self):
        '''
        This method is used to get total balance.
        '''
        return Customer.objects.aggregate(Sum('balance'))['balance__sum']

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        """String for representing the Model object."""
        return self.customer_name

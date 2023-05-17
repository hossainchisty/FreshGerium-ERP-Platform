from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from common.utils import (
    ACCOUNT_STATUS_CHOICE, DISTRICTS, DIVISIONS, INDUSTRYCHOICES,
)
from django.db import models
from utils.models.common_fields import Timestamp


class Account(Timestamp):
    '''Model definition for Account.'''

    name = models.CharField(verbose_name='Name of Account', max_length=25)
    email = models.EmailField()
    phone_number = PhoneNumberField(verbose_name='Phone Number', region="BD", default="+880")
    industry = models.CharField(help_text='Industry Type: ', choices=INDUSTRYCHOICES, max_length=255,  blank=True, null=True)

    country = CountryField(default="BD", verbose_name='Country')
    divistion = models.CharField(verbose_name='Division', choices=DIVISIONS, max_length=25, null=True, blank=True)
    districts = models.CharField(verbose_name='District', choices=DISTRICTS, max_length=25, blank=True, null=True)

    billing_address = models.CharField(verbose_name='Address', max_length=255, blank=True, null=True)
    billing_street = models.CharField(verbose_name='Street', max_length=255, blank=True, null=True)
    billing_city = models.CharField(verbose_name='City', max_length=255, blank=True, null=True)
    billing_state = models.CharField(verbose_name='State', max_length=255, blank=True, null=True)
    billing_postcode = models.CharField(verbose_name='Post/Zip-code', max_length=255, blank=True, null=True)
    billing_country = CountryField(default="BD", verbose_name='Country')

    status = models.CharField(
        choices=ACCOUNT_STATUS_CHOICE, max_length=64, default="open"
    )

    class Meta:
        '''Meta definition for Account.'''
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        '''String represention of Account.'''
        return self.account_name

    @property
    def created_at(self):
        return self.created_at

    def get_complete_address(self):
        '''Concatenates complete address.'''
        address = ''
        if self.billing_address:
            address += self.billing_address
        if self.billing_state:
            if address:
                address += ', ' + self.billing_street
            else:
                address += self.billing_street
        if self.billing_street:
            if address:
                address += ', ' + self.billing_street
            else:
                address += self.billing_street
        if self.billing_city:
            if address:
                address += ', ' + self.billing_city
            else:
                address += self.billing_city
        if self.billing_postcode:
            if address:
                address += ', ' + self.billing_postcode
            else:
                address += self.billing_postcode
        if self.billing_country:
            if address:
                address += ', ' + self.billing_country
            else:
                address += self.billing_country
        return address

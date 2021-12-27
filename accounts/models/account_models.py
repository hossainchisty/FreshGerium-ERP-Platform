from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from utils.bd_districts import bangadesh_districts
from utils.bd_divisions import bangadesh_divisions
from utils.models.common_fields import Timestamp


class Account(Timestamp):
    account_name = models.CharField(verbose_name='Name of Account', max_length=25)
    country = CountryField(default="BD")
    divistion = models.CharField(verbose_name='Division', choices=bangadesh_divisions, max_length=25)
    districts = models.CharField(verbose_name='District', choices=bangadesh_districts, max_length=25)
    phone_number = PhoneNumberField(verbose_name='Phone Number', region="BD", default="+880")
    billing_address = models.TextField()
    INDUSTRY = (
        ('REAL ESTATE', 'REAL ESTATE'),
        ('SOFTWARE', 'SOFTWARE'),
        ('TECHNOLOGY', 'TECHNOLOGY'),
        ('FINANCE', 'FINANCE'),
        ('HEALTHCARE', 'HEALTHCARE'),
        ('INSURANCE', 'INSURANCE'),
        ('LEGAL', 'LEGAL'),
        ('MANUFACTURING', 'MANUFACTURING'),
        ('PUBLISHING', 'PUBLISHING'),
        ('TRANSPORTATION', 'TRANSPORTATION'),
        ('EDUCATION', 'EDUCATION'),
        ('ENTERTAINMENT', 'ENTERTAINMENT'),
        ('MEDIA', 'MEDIA'),
        ('TOURISM', 'TOURISM'),
        ('OTHER', 'OTHER'),
    )
    organization_industry = models.CharField(help_text='Enter Organization Industry Type: ', choices=INDUSTRY, max_length=255)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.account_name

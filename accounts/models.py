from django_countries.fields import CountryField

from django.db import models
from utils.bd_districts import bangadesh_districts
from utils.bd_divisions import bangadesh_divisions


class Account(models.Model):
    account_name = models.CharField(verbose_name='Name of Account', max_length=25)
    account_description = models.TextField(verbose_name='Descrition')
    country = CountryField(default="BD")
    divistion = models.CharField(verbose_name='Division', choices=bangadesh_divisions, max_length=25)
    districts = models.CharField(verbose_name='District', choices=bangadesh_districts, max_length=25)
    account_phone = models.IntegerField()
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

    name_of_account = models.CharField(verbose_name='Name Of Account', max_length=25)
    bank_account_number = models.IntegerField(verbose_name='Bank Account Number')
    bank_name = models.CharField(verbose_name='Bank Name', max_length=25)
    bank_branch = models.CharField(verbose_name='Bank Branch', max_length=25)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.account_name

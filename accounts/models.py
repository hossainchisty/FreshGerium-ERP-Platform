from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Account(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    account_name = models.CharField(verbose_name='Name of Account', max_length=25)
    account_description = models.TextField(verbose_name='Descrition')
    country = CountryField()
    account_phone = models.IntegerField()
    billing_address = models.TextField()
    INDUSTRY = (
        ('FINANCE', 'FINANCE'),
        ('HEALTHCARE', 'HEALTHCARE'),
        ('INSURANCE', 'INSURANCE'),
        ('LEGAL', 'LEGAL'),
        ('MANUFACTURING', 'MANUFACTURING'),
        ('PUBLISHING', 'PUBLISHING'),
        ('REAL ESTATE', 'REAL ESTATE'),
        ('SOFTWARE', 'SOFTWARE'),
    )
    organization_industry = models.CharField(help_text='Enter Organization Industry Type: ', choices=INDUSTRY, max_length=255 )
    
    def __str__(self):
        return self.account_name
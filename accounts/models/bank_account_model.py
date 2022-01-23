from common.utils import ACCOUNT_TYPE
from django.db import models
from utils.models.common_fields import Timestamp


class Bank(Timestamp):
    '''Model definition for Bank.'''

    bank_account_name = models.CharField(verbose_name='Bank Account Name', max_length=25)
    bank_account_number = models.IntegerField(verbose_name='Bank Account Number', unique=True)

    account_type = models.CharField(verbose_name='Bank Account Type', max_length=225, choices=ACCOUNT_TYPE)
    bank_name = models.CharField(verbose_name='Bank Name', max_length=25)
    bank_short_name = models.CharField(verbose_name='Bank Short Name', max_length=5, null=True, blank=True)
    bank_branch = models.CharField(verbose_name='Bank Branch', max_length=25)

    class Meta:
        '''Meta definition for Bank.'''
        verbose_name = 'Bank Account'
        verbose_name_plural = 'Bank Accounts'

    def save(self, *args, **kwargs):
        '''
        On save, update bank account name & bank name capitalize the first letter of each word.
        Example: 'hossain chisty' -> 'Hossain Chisty'
        Example: 'shahjalal islami bank ttd.' -> 'Shahjalal Islami Bank Ltd.'

        '''
        self.bank_account_name = self.bank_account_name.capitalize()
        self.bank_name = self.bank_name.capitalize()
        super(Bank, self).save(*args, **kwargs)

    def __str__(self):
        return self.bank_account_name

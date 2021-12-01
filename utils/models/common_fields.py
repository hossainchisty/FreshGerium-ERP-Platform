from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from utils import random


class Timestamp(models.Model):
    """ Abstract base model for create and update timestamp """
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        abstract = True


class Ledger(Timestamp):
    """ Ledger model for store common information for customer, supplier"""
    date = models.DateField(verbose_name=_('Date'))
    decsription = models.CharField(max_length=255, verbose_name=_('Description'))
    voucher_no = models.CharField(max_length=14, verbose_name=_('Voucher No'), unique=True, default=random.unique_code(14))
    debit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Debit'))
    credit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Credit'))

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.date} - {self.voucher_no}'

    class Meta:
        app_label = 'customers'
        verbose_name = _('Ledger')
        verbose_name_plural = _('Ledgers')

from customers.models import Customer
from django.db import models
from django.db.models import Sum
from products.models import Product
from utils import random
from utils.models.common_fields import Timestamp


class Sale(Timestamp):
    """
    Sale model for storing sale data🛢
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50, choices=(
        ('cash payment', 'Cash Payment'),
        ('credit payment', 'Credit Payment'),
        ('check payment', 'Check payment'),
        ('bank payment', 'Bank Payment'),
    ))
    invoice_number = models.CharField(max_length=10, unique=True, default=random.unique_code(10))

    sale_discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    Shipping_tax = models.DecimalField(max_digits=10, decimal_places=2)
    net_total = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due = models.DecimalField(max_digits=10, decimal_places=2)
    charge = models.DecimalField(max_digits=10, decimal_places=2)


    @property
    def total_balance(self):
        '''
        This method is used to get total balance.
        '''
        return Sale.objects.aggregate(Sum('paid_amount'))['paid_amount__sum']

    def save(self, *args, **kwargs):
        '''
        This method is used to save the data.
        '''
        self.total_balance = self.total_balance + self.due

        super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.customer} {self.date}'

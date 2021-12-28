from customers.models import Customer
from django.db import models
from products.models import Product
from utils import random
from utils.models.common_fields import Timestamp


class Sale(Timestamp):
    """ Sale model for storing sale data🛢 """
    invoice_number = models.CharField(max_length=10, unique=True, default=random.unique_code(10))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    discount = models.DecimalField(default=00.00, max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=(
        ('hand cash', 'Hand Cash'),
        ('cash on delivery', 'Cash On Delivery'),
        ('bKash', 'bKash'),
        ('উপায় (upay)', 'উপায় (upay)'),
        ('nagad', 'Nagad'),
        ('dutch-bangla bank', 'Dutch-Bangla Bank'),
        ('bank payment', 'Bank Payment'),
    ))
    status = models.CharField(max_length=50, choices=(
        ('পাওনা (unpaid)', 'পাওনা (UNPAID)'),
        ('পরিশোধ (paid)', 'পরিশোধ (PAID)'),
    ))
    total_profit = models.DecimalField(default=00.00, max_digits=10, decimal_places=2)
    due = models.DecimalField(default=00.00, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=00.00, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['-date']

    # def save(self, *args, **kwargs):
    #     ''' Calculate sum of total amount with due amount '''
    #     self.total = self.total + self.due

    #     ''' Calculate total profit '''
    #     self.total_profit = self.total - self.discount

    #     super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.customer} {self.date}'

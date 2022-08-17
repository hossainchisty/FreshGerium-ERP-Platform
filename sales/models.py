from decimal import Decimal

from simple_history.models import HistoricalRecords

from customers.models import Customer
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from products.models import Product
from utils import random
from utils.models.common_fields import Timestamp

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Sale(Timestamp):
    """ Sale model for storing sale data🛢 """
    invoice_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()

    '''
    TODO: Future implementation of sale model.

    invoice_date = models.DateTimeField()
    invoice_time = models.DateTimeField()
    invoice_due_date = models.DateField()
    invoice_due_time= models.DateTimeField()
    invoice_subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_tax = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2)
    pdf_file = models.FileField(upload_to='pdfs/')
    '''
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
        ('due', 'Due'),
        ('paid', 'Paid'),
    ))
    is_paid = models.BooleanField(
        verbose_name='Is Paid',
        help_text='Is the sale paid? If yes, the status will be set to paid.',
        default=False,
    )
    discount = models.DecimalField(default=Decimal(0), max_digits=2, decimal_places=0, validators=PERCENTAGE_VALIDATOR)
    due = models.DecimalField(default=00.00, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=00.00, max_digits=10, decimal_places=2)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        """ override the save method for logical purposes """
        # If this flag is True then status will be set to 'paid'.
        if self.is_paid is True:
            # Due amount subtract
            self.due -= self.due
            self.status = 'paid'
        else:
            # If this flag is False then status will be set to 'due'.
            self.status = 'due'
            self.is_paid = False

        # Save the purchase invoice_number, purchase_id with a random code.
        # FIXME: NOT Recommended!!!
        self.invoice_number = random.unique_code(10)
        super(Sale, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        """String for representing the Model object."""
        return f'#{self.invoice_number} number was sold by {self.customer} on {self.date} for {self.product}'

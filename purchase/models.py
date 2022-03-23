from django.db import models
from django.utils.timezone import now
from products.models.product_model import Product
from suppliers.models import Supplier
from utils import random
from utils.models.common_fields import Timestamp


class Purchase(Timestamp):
    """
    Purchase model for storing purchase data🛢
    """
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    invoice_number = models.CharField(max_length=4, unique=True, null=True, blank=True)
    purchase_id = models.CharField(max_length=8, unique=True, null=True, blank=True)
    purchase_date = models.DateField(verbose_name='Purchase Date', default=now)
    payment_options = (
        ('cash payment', 'Cash Payment'),
        ('bank payment', 'Bank Payment'),
        ('online payment', 'Online Payment'),
    )
    payment_method = models.CharField(
        verbose_name='Payment Type',
        max_length=20,
        choices=payment_options,
        default='cash payment',
    )
    details = models.TextField(verbose_name='Details', null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        """ override the save method for logical purposes """
        # Save the purchase invoice_number, purchase_id with a random code.
        self.invoice_number = random.unique_code(4)
        self.purchase_id = random.unique_code(8)
        super(Purchase, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.supplier} {self.purchase_date}'

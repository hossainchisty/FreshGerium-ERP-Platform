from customers.models import Customer
from django.db import models
from products.models import Product
from suppliers.models import Supplier


class Damage(models.Model):
    """
    Damage model for storing product damage history🛢
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    is_customer_notified = models.BooleanField(default=False)
    is_supplier_notified = models.BooleanField(default=False)
    damaged_date = models.DateField()
    reason = [
        ('broken', 'Broken'),
        ('missing', 'Missing'),
        ('expiry dates over', 'Expiry Dates over'),
        ('empty', 'Empty')]
    damaged_reason = models.CharField(max_length=100, choices=reason)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.is_customer_notified:
            return f'{self.customer} due to {self.damaged_reason}, Issue Date: {self.damaged_date}'
        elif self.is_supplier_notified:
            return f'{self.supplier} due to {self.damaged_reason}, Issue Date: {self.damaged_date}'
        else:
            return f'{self.damaged_reason}, Issue Date: {self.damaged_date}'

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
    damaged_date = models.DateField()
    reason = [('broken', 'Broken'), ('missing', 'Missing')]
    damaged_reason = models.CharField(max_length=100, choices=reason)

    def __str__(self):
        return f'{self.product.product_name} - {self.damaged_reason}'

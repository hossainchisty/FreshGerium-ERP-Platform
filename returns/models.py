from customers.models import Customer
from django.db import models
from django.utils import timezone
from products.models import Product
from purchase.models import Purchase
from suppliers.models import Supplier


class Return(models.Model):
    """
    Return model for storing return info🛢
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True)
    reutrn_date = models.DateField(default=timezone.now)
    additional_information = models.TextField(max_length=500, help_text="e.g. My phone has missing headphones", verbose_name="Additional Information (optional)", blank=True, null=True)
    is_returned = models.BooleanField(default=False)
    select_a_reason = [
        ('item is defective or not working', 'Item is defective or not working'),
        ('item or accessory is missing in the', 'Item or accessory is missing in the'),
        ('item has missing freebie', 'Item has missing freebie'),
        ('item does not match decription or picture', 'Item does not match decription or picture'),
        ('i did not order this size', 'I did not order this size'),
        ('i received the wrong item', 'I received the wrong item'),
        ('item does not fit me', 'Item does not fit me'),
        ("don't want to item anymore", "Don't want to item anymore"),
        ('item is damaged/broken/has dent or scratches', 'Item is damaged/broken/has dent or scratches'),
    ]
    return_reason = models.CharField(max_length=100, choices=select_a_reason)

    def __str__(self):
        return f'{self.product.product_name} - {self.return_reason}'

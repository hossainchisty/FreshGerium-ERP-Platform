from customers.models import Customer
from django.db import models
from products.models import Product
from utils.models.common_fields import Timestamp

class Order(Timestamp):
    """
    Damage model for storing order history🛢
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=[('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

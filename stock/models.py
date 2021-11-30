from django.db import models
from products.models import Product
from utils.models.common_fields import Timestamp


class Stock(Timestamp):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    in_qnty = models.IntegerField()
    out_qnty = models.IntegerField()
    stock = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        """String for representing the Model object."""
        return self.product.name

from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField
from simple_history.models import HistoricalRecords

from django.db import models
from suppliers.models import Supplier
from utils import random
from utils.models.common_fields import Timestamp

from .category_model import Category


class Product(Timestamp):
    """ Product model for storing product data🛢 """
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=4, unique=True, null=True, blank=True)
    product_model = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_price = models.DecimalField(max_digits=10, decimal_places=2)
    # FIXME: Add foreign_key with unit model
    unit = models.CharField(max_length=10, choices=[('kg', 'Kilogram'), ('l', 'Liter'), ('pcs', 'Pieces')])
    image = CloudinaryField('Product Images', null=True, blank=True)
    quantity = models.IntegerField(default=0)
    count_sold = models.IntegerField(default=0)
    out_of_stock = models.BooleanField(default=False)
    in_stock = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=[('out of stock', 'Out of Stock'), ('in stock', 'In Stock')], default='In stock')
    recently_sold = models.DateTimeField(null=True, blank=True)
    recently_added = models.DateTimeField(null=True, blank=True)
    recently_viewed = models.DateTimeField(null=True, blank=True)
    recently_updated = models.DateTimeField(null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        """ override the save method for logical purposes """
        if self.in_stock != 0:
            self.status = 'in stock'
            self.out_of_stock = False
        else:
            self.status = 'out of stock'
            # if out of stock, set out_of_stock flag to True
            self.out_of_stock = True
        # Save the product with a random product code.
        self.product_code = random.unique_code(4)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.product_name}'

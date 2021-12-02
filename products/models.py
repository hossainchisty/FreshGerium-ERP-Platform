from django.db import models
from suppliers.models import Supplier
from utils import random
from utils.models.common_fields import Timestamp


class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Product(Timestamp):
    """
    Product model for storing product data🛢
    """
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=4, unique=True, default=random.unique_code(4))
    product_model = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=[('kg', 'Kilogram'), ('l', 'Liter'), ('pcs', 'Pieces')])
    image = models.ImageField(upload_to='product_images/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    @property
    def total_product(self):
        '''
        This method is to calculate the total product
        '''
        return Product.objects.all().count()

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.product_name} Supplier {self.supplier}'

from django.db import models
from django.db.models import Sum
from products.models import Product
from utils.models.common_fields import Timestamp


class Stock(Timestamp):
    """
    Stock model for storing stock data🛢
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    in_qnty = models.IntegerField()
    out_qnty = models.IntegerField()
    stock = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_stock(self):
        '''
        Returns the total stock of the product
        '''
        return Stock.objects.aggregate(Sum('stock'))['stock__sum']

    @property
    def stock_sale_price(self):
        '''
        Returns the stock sale price of the product
        '''
        return self.stock * self.purchase_price

    @property
    def stock_purchase_price(self):
        return self.stock * self.sale_price

    @property
    def total_sales(self):
        ''' Get total sales for a product '''
        return self.sale_price * self.stock

    def __str__(self):
        """String for representing the Model object."""
        return self.product.name

from django.db import models
from customers.models import Customer

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250,null=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)

    @property
    def get_total_amount(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date_created',)
        

class Order(models.Model): 
    STATUS = (
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.product.name
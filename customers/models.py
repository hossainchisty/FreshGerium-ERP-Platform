from django.db import models
from accounts.models import Account

class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    GENDER_SELECT =  (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=200,choices=GENDER_SELECT)
    customer_address = models.TextField()

    previous_balance = models.FloatField()
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE) 

    def __str__(self):
        return self.customer_name




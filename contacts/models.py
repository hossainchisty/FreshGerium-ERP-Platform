from django.db import models
from accounts.models import Account
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.TextField(help_text='Enter your home address:')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


        
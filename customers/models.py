from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from utils.models.common_fields import Timestamp


class Customer(Timestamp):
    customer_name = models.CharField(db_index=True, max_length=200)
    customer_email = models.EmailField()
    GENDER_SELECT = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=200, choices=GENDER_SELECT)
    customer_address = models.CharField(max_length=200)
    mobile_no = PhoneNumberField(default="+8801")
    city = CountryField(default="BD")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    previous_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_customer_url(self):
        return reverse('customer_detail',  kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse('update_customer',  kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('delete_customer',  kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        '''
        Converts a string into all uppercase.
        eg: if customer name is "sakib", then it will save as "Sakib"
        '''
        self.customer_name = self.customer_name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return self.customer_name

    class Meta:
        indexes = [
            models.Index(fields=['customer_name']),
        ]
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

from customers.models import Customer
from django.db import models
from utils.models.common_fields import Timestamp


class Service(Timestamp):
    service_name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    net_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, default=2.00, null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        '''
        Meta class for the Service model.
        '''
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        '''
        Return a string representation of the model object.
        '''
        return self.service_name

    def save(self, *args, **kwargs):
        '''
        Override the save method to calculate the total amount.
        '''
        self.grand_total = self.net_total + self.total_tax
        self.grand_total - self.vat + self.charge
        self.paid_amount = self.grand_total - self.charge
        super(Service, self).save(*args, **kwargs)

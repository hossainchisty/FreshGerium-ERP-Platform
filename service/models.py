from customers.models import Customer
from django.db import models
from utils.models.common_fields import Timestamp


class Service(Timestamp):
    service_name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, blank=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
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
        # Convert charge and grand_total to float if they are strings
        try:
            charge = float(self.charge)
        except (TypeError, ValueError):
            charge = 0.0
        
        try:
            grand_total = float(self.grand_total)
        except (TypeError, ValueError):
            grand_total = 0.0

        # Calculate paid_amount
        self.paid_amount = grand_total - charge
        
        super(Service, self).save(*args, **kwargs)


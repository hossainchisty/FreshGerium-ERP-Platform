from django.db import models
from utils.models.common_fields import Timestamp


class Service(Timestamp):
    service_name = models.CharField(max_length=100)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, default=2.00)

    def __str__(self):
        '''
        Return a string representation of the model object.
        '''
        return self.service_name

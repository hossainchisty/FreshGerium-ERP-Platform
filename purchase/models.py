from django.db import models
from suppliers.models import Supplier
from utils import random
from utils.models.common_fields import Timestamp


class Purchase(Timestamp):
    """
    Purchase model for storing purchase data🛢
    """
    invoice_number = models.CharField(max_length=4, unique=True, default=random.unique_code(4))
    purchase_id = models.CharField(max_length=8, unique=True, default=random.unique_code(8))
    purchase_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.supplier} {self.purchase_date}'

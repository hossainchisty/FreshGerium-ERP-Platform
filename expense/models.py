from django.db import models
from utils.models.common_fields import Timestamp


class Expense(Timestamp):
    """
    Expense model for storing expense data🛢
    """
    date = models.DateField()
    expense_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.expense_type} - {self.amount}"

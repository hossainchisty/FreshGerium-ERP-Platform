from django.db import models
from order.models import Order
from utils.models.common_fields import Timestamp


class Return(Timestamp):
    """
    Return model for storing return info🛢
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    additional_information = models.TextField(max_length=500, help_text="e.g. My phone has missing headphones", verbose_name="Additional Information (optional)", blank=True, null=True)
    select_a_reason = [
        ('item is defective or not working', 'Item is defective or not working'),
        ('item or accessory is missing in the', 'Item or accessory is missing in the'),
        ('item has missing freebie', 'Item has missing freebie'),
        ('item does not match decription or picture', 'Item does not match decription or picture'),
        ('i did not order this size', 'I did not order this size'),
        ('i received the wrong item', 'I received the wrong item'),
        ('item does not fit me', 'Item does not fit me'),
        ("don't want to item anymore", "Don't want to item anymore"),
        ('item is damaged/broken/has dent or scratches', 'Item is damaged/broken/has dent or scratches'),
    ]
    return_reason = models.CharField(max_length=70, choices=select_a_reason)
    is_returned = models.BooleanField(default=False)
    is_returned_by_customer = models.BooleanField(default=False)
    is_returned_by_supplier = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.order} returned due to {self.get_return_reason_display()}'



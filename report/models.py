from django.db import models
from utils.models.common_fields import Timestamp


class Report(Timestamp):
    """
    Damage model for storing report history🛢
    """
    name = models.CharField(max_length=255)
    criteria = models.TextField()

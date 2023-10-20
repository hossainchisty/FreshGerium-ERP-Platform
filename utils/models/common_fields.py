from authenticator.models import User
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

__author__ = "Hossain Chisty"


class Timestamp(models.Model):
    """ Abstract base model for create and update timestamp and user for all models. """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'), null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        abstract = True


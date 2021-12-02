from django.contrib import admin
from utils.models.common_fields import Ledger

from .models import Customer

admin.site.register(Ledger)
admin.site.register(Customer)

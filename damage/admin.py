from import_export.admin import ImportExportModelAdmin

from damage.models import Damage
from django.contrib import admin


@admin.register(Damage)
class DamageAdmin(ImportExportModelAdmin):
    list_display = ('product', 'damaged_date', 'damaged_reason', 'customer', 'supplier')

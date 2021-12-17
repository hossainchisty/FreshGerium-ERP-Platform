from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from expense.models import Expense


@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):
    pass



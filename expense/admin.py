from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from expense.models import Category, Expense


@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ('date', 'expense_type', 'amount', 'category')


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name',)

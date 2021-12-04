from django.urls import path
from expense.views.manage_expense_views import (
    ExpenseItem, ExpenseStatement, ManageExpense,
)

urlpatterns = [
    path('', ManageExpense.as_view(), name='manage_expense'),
    path('items/', ExpenseItem.as_view(), name='expense_item'),
    path('statement/', ExpenseStatement.as_view(), name='expense_statement'),
]

from django.urls import path
from expense.views.add_expense_views import CreateExpense
from expense.views.donwload_expense_pdf import DownloadExpensePDF
from expense.views.expense_pdf_views import ViewExpensePDF
from expense.views.export_expense_csv_views import DownloadExpenseCSV
from expense.views.manage_expense_views import (
    ExpenseItem, ExpenseStatement, ManageExpense,
)

urlpatterns = [
    path('', ManageExpense.as_view(), name='manage_expense'),
    path('add/', CreateExpense.as_view(), name='add_expense'),
    path('items/', ExpenseItem.as_view(), name='expense_item'),
    path('statement/', ExpenseStatement.as_view(), name='expense_statement'),
    path('export/', DownloadExpenseCSV.as_view(), name='download_expense_csv'),
    path('pdf/', ViewExpensePDF.as_view(), name='view_expense_pdf'),
    path('pdf/download/', DownloadExpensePDF.as_view(), name="pdf_expense_download")
]

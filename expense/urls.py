from django.urls import path
from expense.views.add_expense_views import CreateExpense
from expense.views.delete_expense_views import DeleteExpense
from expense.views.download_expense_pdf import DownloadExpensePDF
from expense.views.expense_pdf_views import ViewExpensePDF
from expense.views.export_expense_csv_views import DownloadExpenseCSV
from expense.views.export_expense_excle_views import DownloadExpenseEXCLE
from expense.views.manage_expense_views import (
    ExpenseItem, ExpenseStatement, ManageExpense,
)
from expense.views.update_expense_views import UpdateExpense

urlpatterns = [
    path('', ManageExpense.as_view(), name='manage_expense'),
    path('add/', CreateExpense.as_view(), name='add_expense'),
    path('delete/<pk>', DeleteExpense.as_view(), name='delete_expense'),
    path('update/<pk>', UpdateExpense.as_view(), name='update_expense'),
    path('items/', ExpenseItem.as_view(), name='expense_item'),
    path('statement/', ExpenseStatement.as_view(), name='expense_statement'),
    path('export/csv/', DownloadExpenseCSV.as_view(), name='download_expense_csv'),
    path('export/excle/', DownloadExpenseEXCLE.as_view(), name='download_expense_excle'),
    path('pdf/', ViewExpensePDF.as_view(), name='view_expense_pdf'),
    path('pdf/download/', DownloadExpensePDF.as_view(), name="pdf_expense_download")
]

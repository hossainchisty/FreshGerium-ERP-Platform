from django.urls import path
from expense.views.add_expense_views import CreateExpense
from expense.views.donwload_expense_pdf import DownloadPDF
from expense.views.expense_pdf_views import ViewPDF
from expense.views.export_expense_csv_views import DownloadExpenseCSV
from expense.views.manage_expense_views import (
    ExpenseItem, ExpenseStatement, ManageExpense,
)

urlpatterns = [
    path('', ManageExpense.as_view(), name='manage_expense'),
    path('add/', CreateExpense.as_view(), name='add_expense'),
    path('items/', ExpenseItem.as_view(), name='expense_item'),
    path('statement/', ExpenseStatement.as_view(), name='expense_statement'),
    path('download-as-csv/', DownloadExpenseCSV.as_view(), name='download_expense_csv'),
    path('view/pdf/', ViewPDF.as_view(), name='view_pdf'),
    path('pdf_download/', DownloadPDF.as_view(), name="pdf_download")
]

import csv

from django.http import HttpResponse
from django.views.generic import View
from expense.models import Expense


class DownloadExpenseCSV(View):
    '''
    Automaticly download expense data as CSV file.
    '''
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        write = csv.writer(response)
        write.writerow(["Date", "Expense Type", "Amount"])

        for expense in Expense.objects.all():
            write.writerow([expense.date, expense.expense_type, expense.amount])
            response["Content-Disposition"] = "attachment; filename=expense-data.csv"
            return response

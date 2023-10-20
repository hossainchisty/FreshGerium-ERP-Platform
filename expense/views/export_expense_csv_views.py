import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View
from expense.models import Expense


class DownloadExpenseCSV(LoginRequiredMixin, View):
    '''
    Automaticly download expense data as CSV file.
    '''
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        write = csv.writer(response)
        write.writerow(["Date", "Expense Type", "Category", "Amount"])

        for expense in Expense.objects.all():
            write.writerow([expense.date, expense.expense_type, expense.category.name, expense.amount])
            response["Content-Disposition"] = "attachment; filename=expense-data.csv"
            return response

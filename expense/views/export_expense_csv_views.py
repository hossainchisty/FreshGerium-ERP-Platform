import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from expense.models import Expense
from utils.helper.decorators.filter import _currentUser


class DownloadExpenseCSV(LoginRequiredMixin, View):
    '''
    Automaticly download expense data as CSV file.
    '''
    @method_decorator(_currentUser())
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        write = csv.writer(response)
        write.writerow(["Date", "Expense Type", "Amount"])

        for expense in Expense.objects.all():
            write.writerow([expense.date, expense.expense_type, expense.amount])
            response["Content-Disposition"] = "attachment; filename=expense-data.csv"
            return response

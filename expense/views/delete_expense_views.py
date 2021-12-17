from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from expense.models import Expense


class DeleteExpense(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_item')

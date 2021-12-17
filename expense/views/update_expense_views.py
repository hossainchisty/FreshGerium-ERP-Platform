from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from expense.models import Expense


class UpdateExpense(UpdateView):
    model = Expense
    fields = ['expense_type']
    template_name = 'expense/expense_form.html'
    success_url = reverse_lazy('expense_item')

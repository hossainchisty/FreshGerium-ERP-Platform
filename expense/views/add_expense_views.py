
from django.shortcuts import redirect, render
from django.views import View
from expense.models import Expense


class CreateExpense(View):
    '''
    Intentionally simple parent class for all views.
    '''
    def get(self, request, *args, **kwargs):
        return render(request,  'expense/add_expense.html')

    def post(self, request, *args, **kwargs):
        ''' Create a new expense '''
        expense_date = request.POST.get('expense_date')
        expense_type = request.POST.get('expense_type')
        expense_amount = request.POST.get('expense_amount')
        expense = Expense(date=expense_date, expense_type=expense_type, amount=expense_amount)
        expense.save()
        """Provide a redirect on GET request."""
        return redirect('manage_expense')

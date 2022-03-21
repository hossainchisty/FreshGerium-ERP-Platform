from django.shortcuts import redirect, render
from django.views import View
from expense.models import Category, Expense


class CreateExpense(View):
    '''
    Intentionally simple parent class for all views.
    '''

    def get(self, request, *args, **kwargs):
        ''' Get the expense form '''
        categories = Category.objects.all()
        return render(request,  'expense/add_expense.html', {'categories': categories})

    def post(self, request, *args, **kwargs):
        ''' Create a new expense '''
        expense_date = request.POST.get('expense_date')
        expense_type = request.POST.get('expense_type')
        expense_amount = request.POST.get('expense_amount')
        categories = request.POST.get('categories')
        expense = Expense(date=expense_date, expense_type=expense_type, amount=expense_amount, category=categories)

        expense.save()
        """Provide a redirect on GET request."""
        return redirect('manage_expense')

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View
from expense.models import Expense


class ManageExpense(View):
    '''
    List all Expense date expense type and amount.
    '''
    def get(self, request):
        expenses_list = Expense.objects.all().order_by('-id')
        paginator = Paginator(expenses_list, 20) # Show 20 Expense list per page.
        page_number = request.GET.get('page')
        expenses = paginator.get_page(page_number)
        context = {
            'expenses': expenses
        }
        return render(request, 'expense/manage_expense.html', context)


class ExpenseStatement(View):
    '''
    TODO:
    1. Need to add seach wth date range and expense type
    2. Need to add pagination[20 items per page] / Not mandatory
    '''
    def get(self, request):
        return render(request, 'expense/expense_statement.html')


class ExpenseItem(View):
    '''
    TODO:
    1. Need to show the expense item action buttons[Edit, Delete]
     - CSV,pdf,print
    2. Need to add pagination[20 items per page]
    '''
    def get(self, request):
        return render(request, 'expense/expense_item.html')

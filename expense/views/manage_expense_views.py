from django.shortcuts import render
from django.views.generic import View


class ManageExpense(View):
    '''
    TODO:
    1. Add Expense Statement
    2. Edit Expense Statement
    3. Delete Expense Statement
    4. Need to add pagination[10 items per page]
    '''
    def get(self, request):
        return render(request, 'expense/manage_expense.html')


class ExpenseStatement(View):
    '''
    TODO:
    1. Need to add seach wth date range and expense type
    2. Need to add pagination[10 items per page] / Not mandatory
    '''
    def get(self, request):
        return render(request, 'expense/expense_statement.html')


class ExpenseItem(View):
    '''
    TODO:
    1. Need to show the expense item action buttons[Edit, Delete]
     - CSV,pdf,print
    2. Need to add pagination[10 items per page]
    '''
    def get(self, request):
        return render(request, 'expense/expense_item.html')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View
from expense.models import Category, Expense


@method_decorator(cache_page(60 * 3), name='dispatch')
class ManageExpense(LoginRequiredMixin, View):
    '''
    List all Expense date expense type and amount.
    '''
    def get(self, request):
        expenses_list = Expense.objects.all().order_by('-id')
        paginator = Paginator(expenses_list, 20)
        page_number = request.GET.get('page')
        expenses = paginator.get_page(page_number)
        context = {
            'expenses': expenses
        }
        return render(request, 'expense/manage_expense.html', context)





class ExpenseItem(LoginRequiredMixin, View):
    '''
    Expense item action buttons[Edit, Delete]
     - CSV,pdf,print
    TODO: 2. Need to add pagination[20 items per page]
    '''
    def get(self, request):
        expenses_list = Expense.objects.all().order_by('-id')
        paginator = Paginator(expenses_list, 20)
        page_number = request.GET.get('page')
        expenses = paginator.get_page(page_number)
        context = {
            'expenses': expenses
        }
        return render(request, 'expense/expense_item.html', context)


class ExpenseCategory(LoginRequiredMixin, View):
    ''' Expense category list '''
    def get(self, request):
        category_list = Category.objects.all().order_by('-id')
        paginator = Paginator(category_list, 20)
        page_number = request.GET.get('page')
        categories = paginator.get_page(page_number)
        context = {
            'categories': categories
        }
        return render(request, 'expense/category_item.html', context)

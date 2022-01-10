
from django.shortcuts import redirect, render
from django.views import View
from expense.models import Category


class CreateCategory(View):
    '''
    Intentionally simple parent class for all views.
    '''
    def get(self, request, *args, **kwargs):
        return render(request,  'expense/add_category.html')

    def post(self, request, *args, **kwargs):
        ''' Create a new expense '''
        category_name = request.POST.get('category_name')
        category = Category(name=category_name)
        category.save()
        """Provide a redirect on GET request."""
        return redirect('expense_category')

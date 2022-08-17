from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from expense.models import Expense
from utils.helper.decorators.filter import _currentUser
from utils.render_to_pdf import generate_pdf


class ViewExpensePDF(LoginRequiredMixin, View):
    ''' This view will show pdf '''
    @method_decorator(_currentUser())
    def get(self, request, *args, **kwargs):
        expense = Expense.objects.all().order_by('-id')
        pdf = generate_pdf('expense/pdf/expense_pdf.html', {'expense': expense})
        return HttpResponse(pdf, content_type='application/pdf')

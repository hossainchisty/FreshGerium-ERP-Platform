from datetime import date

from django.http import HttpResponse
from django.views.generic import View
from expense.models import Expense
from utils.render_to_pdf import generate_pdf


class DownloadPDF(View):
    '''
    Automaticly downloads to PDF file.
    '''
    def get(self, request, *args, **kwargs):
        expense = Expense.objects.all().order_by('-id')
        pdf = generate_pdf('expense/pdf/expense_pdf.html', {'expense': expense})
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Expense-Data-%s.pdf" % date.today()
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response

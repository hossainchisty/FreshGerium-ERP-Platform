from datetime import date

from django.http import HttpResponse
from django.views.generic import View
from stock.models import Stock
from utils.render_to_pdf import generate_pdf


class DownloadStockPDF(View):
    '''
    Automaticly downloads to PDF file.
    '''
    def get(self, request, *args, **kwargs):
        stock = Stock.objects.all().order_by('-id')
        pdf = generate_pdf('stock/pdf/stock_pdf.html', {'stock': stock})
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Stock-Data-%s.pdf" % date.today()
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response

from django.http import HttpResponse
from django.views.generic import View
from stock.models import Stock
from utils.render_to_pdf import generate_pdf


class ViewStockPDF(View):
	def get(self, request, *args, **kwargs):
		stock = Stock.objects.all().order_by('-id')
		pdf = generate_pdf('stock/pdf/stock_pdf.html', {'stock': stock})
		return HttpResponse(pdf, content_type='application/pdf')

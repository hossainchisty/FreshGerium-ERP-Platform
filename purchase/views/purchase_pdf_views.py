from django.http import HttpResponse
from django.views.generic import View
from purchase.models import Purchase
from utils.render_to_pdf import generate_pdf


class ViewPurchasePDF(View):
	def get(self, request, *args, **kwargs):
		purchase = Purchase.objects.all().order_by('-id')
		pdf = generate_pdf('purchase/pdf/purchase_pdf.html', {'purchase': purchase})
		return HttpResponse(pdf, content_type='application/pdf')

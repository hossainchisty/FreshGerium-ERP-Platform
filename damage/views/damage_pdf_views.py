from damage.models import Damage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View
from utils.render_to_pdf import generate_pdf


class ViewDamagePDF(LoginRequiredMixin, View):
	'''
	View damage data as PDF file.
	'''
	def get(self, request, *args, **kwargs):
		damage = Damage.objects.all().order_by('-id')
		pdf = generate_pdf('damage/pdf/damage_pdf.html', {'damage': damage})
		return HttpResponse(pdf, content_type='application/pdf')

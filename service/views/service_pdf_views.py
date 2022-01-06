from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from service.models import Service
from utils.helper.decorators.filter import _currentUser
from utils.render_to_pdf import generate_pdf


class ViewServicePDF(LoginRequiredMixin, View):
	''' View Service PDF '''
	@method_decorator(_currentUser())
	def get(self, request, *args, **kwargs):
		service = Service.objects.all().order_by('-id')
		pdf = generate_pdf('service/pdf/service_pdf.html', {'service': service})
		return HttpResponse(pdf, content_type='application/pdf')

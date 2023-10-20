from datetime import date

from order.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.helper.decorators.filter import _currentUser
from utils.render_to_pdf import generate_pdf


class DownloadOrderPDF(LoginRequiredMixin, View):
    '''
    Automaticly downloads to PDF file.
    '''
    @method_decorator(_currentUser())
    def get(self, request, *args, **kwargs):
        order = Order.objects.all().order_by('-id')
        pdf = generate_pdf('order/pdf/order_pdf.html', {'order': order})
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Order-Data-%s.pdf" % date.today()
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response

from datetime import date

from damage.models import Damage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View
from utils.render_to_pdf import generate_pdf


class DownloadDamagePDF(LoginRequiredMixin, View):
    '''
    Automaticly downloads to PDF file.
    '''
    def get(self, request, *args, **kwargs):
        damage = Damage.objects.all().order_by('-id')
        pdf = generate_pdf('damage/pdf/damage_pdf.html', {'damage': damage})
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Damage-Data-%s.pdf" % date.today()
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response

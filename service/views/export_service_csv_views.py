import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from service.models import Service
from utils.helper.decorators.filter import _currentUser


class DownloadServiceCSV(LoginRequiredMixin, View):
    '''
    Automaticly download service data as CSV file.
    '''
    @method_decorator(_currentUser())
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        write = csv.writer(response)
        write.writerow(["Service", "Charge", "Description", "VAT"])

        for service in Service.objects.all():
            write.writerow([service.service_name, service.charge, service.description, service.vat])
            response["Content-Disposition"] = "attachment; filename=Service-data.csv"
            return response

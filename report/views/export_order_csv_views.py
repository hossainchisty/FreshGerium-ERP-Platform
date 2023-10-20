import csv

from damage.models import Damage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.helper.decorators.filter import currentUser


class DownloadDamageCSV(LoginRequiredMixin, View):
    '''
    Automaticly download damage data as CSV file.
    '''
    @method_decorator(currentUser)
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        write = csv.writer(response)
        write.writerow(["Product", "Customer", "Supplier", "Damaged Date", "Damaged Reason", "Note"])

        for items in Damage.objects.all():
            write.writerow([items.product, items.customer, items.supplier, items.damaged_date, items.damaged_reason, items.note])
            response["Content-Disposition"] = "attachment; filename=Damage-data.csv"
            return response

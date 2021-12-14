
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from service.models import Service


class ServiceUpdate(UpdateView):
    model = Service
    fields = ['service_name', 'charge', 'description', 'vat']
    template_name = 'service/update_service_form.html'
    success_url = reverse_lazy('manage_service')

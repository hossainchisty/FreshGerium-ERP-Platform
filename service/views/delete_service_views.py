from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from service.models import Service


class DeleteService(DeleteView):
    model = Service
    success_url = reverse_lazy('manage_service')

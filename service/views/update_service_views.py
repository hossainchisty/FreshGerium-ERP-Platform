
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from service.models import Service


class ServiceUpdate(UpdateView):
    model = Service
    fields = ['service_name', 'charge', 'description', 'vat']
    template_name = 'service/update_service_form.html'
    success_url = reverse_lazy('manage_service')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this service.")
        return obj

from damage.models import Damage
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class UpdateDamage(UpdateView):
    model = Damage
    fields = '__all__'
    template_name = 'damage/damage_form.html'
    success_url = reverse_lazy('damage_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this damage.")
        return obj

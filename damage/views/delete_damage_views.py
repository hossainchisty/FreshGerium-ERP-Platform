from damage.models import Damage
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class DeleteDamage(DeleteView):
    model = Damage
    success_url = reverse_lazy('damage_list')

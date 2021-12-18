from damage.models import Damage
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class UpdateDamage(UpdateView):
    model = Damage
    fields = '__all__'
    template_name = 'damage/damage_form.html'
    success_url = reverse_lazy('damage_list')

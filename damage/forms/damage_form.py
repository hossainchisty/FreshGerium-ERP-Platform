from damage.models import Damage
from django.forms import ModelForm


class DamageForm(ModelForm):
    ''' Form asking for the Damge Information '''
    class Meta:
        model = Damage
        fields = ['product', 'customer', 'supplier', 'damaged_date', 'damaged_reason']

from damage.models import Damage
from django.forms import ModelForm
from django.forms.widgets import DateInput


class DamageForm(ModelForm):
    ''' Form asking for the Damge Information '''
    class Meta:
        model = Damage
        fields = ['product', 'customer', 'supplier', 'damaged_date', 'damaged_reason']
        widgets = {
            'damaged_date': DateInput(attrs={'type': 'date'})
        }

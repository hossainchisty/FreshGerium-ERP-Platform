from damage.models import Damage
from django.forms import ModelForm


class DamageForm(ModelForm):
    ''' Damge Form for damage Model '''
    class Meta:
        model = Damage
        fields = '__all__'

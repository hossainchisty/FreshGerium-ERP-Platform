from django.forms import ModelForm
from suppliers.models import Supplier


class SupplierForm(ModelForm):
    ''' Form asking for create supplier Information '''
    class Meta:
        model = Supplier
        fields = '__all__'
        exclude = ['user', 'supplier_ledger']

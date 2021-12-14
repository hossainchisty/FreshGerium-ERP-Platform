from django.forms import ModelForm
from django.forms.widgets import DateInput
from purchase.models import Purchase


class PurchaseForm(ModelForm):
    ''' Purchase Form for Purchase Model '''
    class Meta:
        model = Purchase
        fields = ['invoice_number', 'purchase_id', 'supplier', 'purchase_date', 'total_amount']
        widgets = {
            'purchase_date': DateInput(attrs={'type': 'date'})
        }

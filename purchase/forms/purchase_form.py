from django.forms import ModelForm
from django.forms.widgets import DateInput
from purchase.models import Purchase


class PurchaseForm(ModelForm):
    ''' Form asking for the Purchase Information '''
    class Meta:
        model = Purchase
        fields = ['product', 'supplier', 'purchase_date', 'payment_method', 'details', 'discount', 'paid_amount', 'due_amount', 'total_amount']
        widgets = {
            'purchase_date': DateInput(attrs={'type': 'date'})
        }

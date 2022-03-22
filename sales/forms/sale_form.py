from django.forms import ModelForm
from django.forms.widgets import DateInput
from sales.models import Sale


class SaleForm(ModelForm):
    ''' Form asking for the Sales Information '''
    class Meta:
        model = Sale
        fields = ['customer', 'product', 'date', 'payment_method', 'is_paid', 'discount', 'due', 'total']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }

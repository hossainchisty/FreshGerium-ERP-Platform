from order.models import Order
from django.forms import ModelForm


class OrderForm(ModelForm):
    ''' Form asking for the Order Information '''
    class Meta:
        model = Order
        fields = ['product', 'customer', 'status', 'quantity','total_amount']

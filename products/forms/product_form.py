from django.forms import ModelForm
from products.models import Product


class ProductForm(ModelForm):
    ''' Form asking for create products '''
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user', ]

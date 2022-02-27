from ckeditor.widgets import CKEditorWidget

from django import forms
from django.forms import ModelForm
from products.models import Product


class ProductForm(ModelForm):
    ''' Form asking for create products '''
    product_description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user', 'product_code', 'quantity', 'count_sold', 'out_of_stock', 'status', 'recently_sold', 'recently_added', 'recently_viewed', 'recently_updated']

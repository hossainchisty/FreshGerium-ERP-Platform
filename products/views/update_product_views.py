from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from products.models.product_model import Product


class UpdateProductView(UpdateView):
    """ Update product view """
    model = Product
    fields = ['product_name', 'product_model', 'product_description', 'price', 'supplier_price', 'unit', 'image', 'in_stock', 'country', 'category', 'supplier']
    template_name = 'products/update_product.html'
    success_url = reverse_lazy('product_list')

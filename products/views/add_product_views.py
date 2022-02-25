from datetime import datetime

from django.shortcuts import redirect, render
from django.views.generic import View
from products.forms.product_form import ProductForm


class CreateProduct(View):
    '''
    Intentionally simple parent class for all views.
    '''

    def get(self, request, *args, **kwargs):
        return render(request,  'products/add_product.html', {'form': ProductForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new Product '''
        form = ProductForm(request.POST, request.FILES)
        # Automatically set to the currently logged-in user
        form.instance.user = request.user
        if form.is_valid():
            form.instance.recently_added = datetime.now()
            form.save()
            """Provide a redirect on GET request."""
            return redirect('product_list')
        else:
            return render(request, 'products/add_product.html', {'form': form})

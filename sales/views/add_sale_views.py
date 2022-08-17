from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View
from sales.forms.sale_form import SaleForm


class CreateSale(View):
    ''' This class is used to create a new sales. '''

    def get(self, request, *args, **kwargs):
        ''' Get the sales form '''
        return render(request,  'sales/add_sales.html', {'forms': SaleForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new sales '''

        form = SaleForm(request.POST)
        with transaction.atomic():
            # Automatically set to the currently logged-in user
            form.instance.user = request.user
            if form.is_valid():
                form.save()
                """Provide a redirect on GET request."""
                return redirect('sales_list')
            else:
                return render(request, 'sales/add_sales.html', {'forms': form})
            """Provide a redirect on GET request."""
            return redirect('sales_list')

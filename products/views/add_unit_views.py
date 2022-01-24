
from django.shortcuts import redirect, render
from django.views import View
from products.models import Unit


class CreateUnit(View):
    '''
    Intentionally simple parent class for all views.
    '''

    def get(self, request, *args, **kwargs):
        return render(request,  'products/add_unit.html')

    def post(self, request, *args, **kwargs):
        ''' Create a new Unit '''
        unit_name = request.POST.get('unit_name')
        unit = Unit(name=unit_name)
        unit.save()
        """Provide a redirect on GET request."""
        return redirect('product_list')

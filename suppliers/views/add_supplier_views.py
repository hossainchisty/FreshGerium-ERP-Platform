from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View
from suppliers.forms.suppliers_form import SupplierForm


class AddSupplier(LoginRequiredMixin, View):
    '''
    Intentionally simple parent class for all views.
    '''

    def get(self, request):
        ''' Get the suppliers form '''
        return render(request, 'suppliers/add_suppliers.html', {'form': SupplierForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new suppliers '''
        form = SupplierForm(request.POST)
        # Automatically set to the currently logged-in user
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            '''Provide a redirect on GET request.'''
            return redirect('suppliers_list')
        else:
            return render(request, 'suppliers/add_suppliers.html', {'form': form})

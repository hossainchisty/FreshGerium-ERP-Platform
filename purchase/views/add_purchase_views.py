from django.shortcuts import redirect, render
from django.views import View
from purchase.forms.purchase_form import PurchaseForm


class CreatePurchase(View):
    ''' Create a new purchase '''

    def get(self, request, *args, **kwargs):
        return render(request,  'purchase/add_purchase.html', {'forms': PurchaseForm()})

    def post(self, request, *args, **kwargs):
        ''' Create a new purchase '''
        form = PurchaseForm(request.POST)
        # Automatically set to the currently logged-in user
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            ''' Provide a redirect on GET request.'''
            return redirect('manage_purchase')
        else:
            return render(request, 'purchase/add_purchase.html', {'forms': form})

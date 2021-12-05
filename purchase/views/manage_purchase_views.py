from django.shortcuts import render
from django.views.generic import View


class ManagePurchase(View):
    '''
    TODO:
    1. Need to show the purchase item action buttons[Edit]
     - view details
    2. Need to add pagination[10 items per page]
    '''
    def get(self, request):
        return render(request, 'purchase/manage_purchase.html')

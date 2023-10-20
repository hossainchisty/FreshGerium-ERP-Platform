from order.forms.order_form import OrderForm
from django.shortcuts import redirect, render
from django.views import View


class CreateOrder(View):
    ''' Create a new order '''

    def get(self, request, *args, **kwargs):
        ''' Respond to GET request '''
        return render(request,  'order/add_order.html', {'forms': OrderForm()})

    def post(self, request, *args, **kwargs):
        ''' Respond to POST request '''
        form = OrderForm(request.POST)
        # Automatically set to the currently logged-in user
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            ''' Provide a redirect on GET request. '''
            return redirect('order_list')
        else:
            return render(request, 'order/add_order.html', {'forms': form})

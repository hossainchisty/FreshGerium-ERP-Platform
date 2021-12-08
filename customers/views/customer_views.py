from customers.models import Customer
from django.shortcuts import render
from django.views.generic import View


class CustomerList(View):
    def get(self, request):
        '''
        This will reutrn list of customer
        '''
        customers = Customer.objects.all().order_by('-id')

        context = {
            'customers': customers
        }
        return render(request, 'customers/customer.html', context)

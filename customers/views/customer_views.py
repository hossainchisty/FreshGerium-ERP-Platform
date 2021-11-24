from django.shortcuts import render


def customer(request):
    return render(request, 'customers/customer.html')

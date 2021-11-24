from django.shortcuts import render


def contact(request):
    return render(request, 'contacts/contact.html')

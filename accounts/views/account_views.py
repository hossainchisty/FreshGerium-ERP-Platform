from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View


class AccountView(View):
    def get(self, request):
        ''' This will return the accounts list '''
        return render(request, 'accounts/accounts.html')

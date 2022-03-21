from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def account_data(request):
    '''
    View that shows the user's account data.
    '''
    return render(request, 'profiles/account_data.html')

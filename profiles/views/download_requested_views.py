from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def download_requested(request):
    '''
    TODO: Need to start building user data 
    '''
    return render(request, 'profiles/download_requested.html')

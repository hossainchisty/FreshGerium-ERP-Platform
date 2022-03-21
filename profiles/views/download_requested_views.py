from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def download_requested(request):
    '''
    TODO: Need to start building user data user will receive a ZIP file which contains a bunch of JSON text files
    '''
    return render(request, 'profiles/download_requested.html')

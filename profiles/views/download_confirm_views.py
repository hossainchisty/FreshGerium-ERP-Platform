from django.shortcuts import render


def download_confirm(request):
    '''
    TODO: User can download the file after confirming the download.
    File would be in zip format
    '''
    return render(request, 'profiles/download_confirm.html')

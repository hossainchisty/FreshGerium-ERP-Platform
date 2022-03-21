from authenticator.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def data_view(request):
    '''
    View that shows the user's account data.
    '''
    return render(request, 'profiles/view_logout.html')

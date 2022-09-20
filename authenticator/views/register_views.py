import uuid

from authenticator.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.db import transaction
from django.shortcuts import redirect, render

from .email_verify import sendVerifyToken


def RegisterView(request):
    ''' Sign up new user to freshdesk '''
    if request.method == 'POST':
        owner = request.POST.get('OwnerName')
        organization = request.POST.get('OrganizationName')
        mobile = request.POST.get('MobileNumber')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        repeatPassword = request.POST.get('RepeatPassword')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists.')
            return redirect('sign-up')

        if User.objects.filter(mobile_number=mobile).exists():
            messages.info(request, 'Mobile number already exists.')
            return redirect('sign-up')

        if password and repeatPassword:
            if password != repeatPassword:
                messages.info(request, "The two password fields didn't match.")
                return redirect('sign-up')
        print('Passed all errors')
        with transaction.atomic():
            # If something went wrong/fails
            # The database will perform a rollback by itself.
            auth_token = str(uuid.uuid4())
            user_create = User.objects.create(owner_name=owner, organization_name=organization, mobile_number=mobile, email=email, token=auth_token)
            user_create.set_password(password)
            user_create.save()
            # to get the domain of the current site
            current_site = get_current_site(request).domain
            sendVerifyToken(email, auth_token, current_site)
            return redirect('token_send')
    return render(request, 'authenticator/register.html')


def Tokensend(request):
    '''Let user to check there email for further instruction '''
    return render(request, 'authenticator/token_send.html')


def Success(request):
    ''' When user successfully verify there email '''
    return render(request, 'authenticator/success.html')

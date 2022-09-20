from authenticator.models import User
from django.contrib import messages
from django.shortcuts import redirect


def VerifyToken(request, token):
    ''' Verify user token '''
    user_profile = User.objects.filter(token=token).first()
    if user_profile.is_verified:
        messages.info(request, 'Email already verified')
        return redirect('sign-in')
    if user_profile:
        user_profile.is_verified = True
        user_profile.save()
        messages.success(request, 'Your account has been verified.')
        return redirect('success')
    else:
        messages.info(request, 'Something went worng.')

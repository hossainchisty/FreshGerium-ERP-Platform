from authenticator.models import User
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from utils.email_thread import EmailThread


class PasswordResetView(View):
    '''
    Password reset with email address
    '''

    def get(self, request, *args, **kwargs):
        return render(request, 'authenticator/password/forgot-password.html', {'form': PasswordResetForm()})

    def post(self, request, *args, **kwargs):
        ''' '''
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    email_template_name = "authenticator/password/email/password_reset_email.html"
                    current_site = Site.objects.get_current()
                    email_context = {
                        'email': user.email,
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    body = render_to_string(email_template_name, email_context)
                    email = EmailMessage(
                        subject="Password Reset Requested for your Freskdesk Account.",
                        body=body,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[user.email],
                    )
                    email.content_subtype = "HTML"
                    try:
                        EmailThread(email).start()
                        return redirect('password_reset_done')
                        messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    except Exception as e:
                        print(e)
                        messages.error(request, "Email sending failed. Please try again.")
                return redirect('dashboard')
            else:
                messages.error(request, "Email address not found.")
        return render(request, 'authenticator/password/forgot-password.html', {'form': form})

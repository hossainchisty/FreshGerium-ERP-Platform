
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def sendVerifyToken(email, token, current_site):
    body = render_to_string('authenticator/email/verify_email.html', {'domain': current_site, 'token': token, 'email': email})

    mail = EmailMessage(
        subject='Verification Needed!',
        body=body,
        # FIXME: EMAIL_BACKEND Is for testing
        from_email=settings.EMAIL_BACKEND,
        to=[email],
    )
    mail.content_subtype = 'html'
    # TODO: Recommendation is use celery for background tasks.
    mail.send()

from authenticator.models import User
from core.middleware import RequestMiddleware
from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from utils.email_thread import EmailThread


@receiver(pre_save, sender=User)
def detect_password_change(sender, instance, **kwargs):
    """
    Checks if the user changed his/her password and sends an email to the user to alert.
    """
    if instance._password is None:
        return f"{instance.email}'s password is not changed."
    try:
        user = User.objects.get(id=instance.id)
        # Get current request object
        request = RequestMiddleware(get_response=None)
        request = request.thread_local.current_request
        user_ip_address = request.session['user_ip']
        timezone = request.session['timezone']

        body = render_to_string("settings/email/security_alert_after_changed_password.html",
                                {"user": user, "user_ip_address": user_ip_address, "timezone": timezone})
        email = EmailMessage(
            subject="Your Freskdesk password was changed.",
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
        )
        email.content_subtype = "HTML"
        EmailThread(email).start()
    except User.DoesNotExist:
        return f'User with id {instance.id} does not exist'

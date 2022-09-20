from authenticator.models import User
# from common.utils import get_client_ip
# from core.middleware.requests import RequestMiddleware
# from django.conf import settings
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.signals import user_logged_in, user_logged_out
# from django.contrib.sessions.models import Session
# from django.core.mail import EmailMessage
# from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# from django.template.loader import render_to_string
from django.utils import timezone

# from utils.email_thread import EmailThread


@receiver(user_logged_in, sender=User)
def track_user_login_datetime(sender, request, user, **kwargs):
    request.user.is_verified = True
    request.user.login_datetime = timezone.now()
    request.user.save()
    print('Successfully login in {} and saved logout datetime'.format(user.email))


@receiver(user_logged_out, sender=User)
def track_user_logout_datetime(sender, request, user, **kwargs):
    request.user.is_verified = True
    request.user.logout_datetime = timezone.now()
    request.user.save()
    print('Successfully logged out user {} and saved logout datetime'.format(user.email))


# @receiver(user_logged_in)
# def send_new_device_login_alert(sender, user, reqeust, **kwargs):
#     # Get current request object
#     request = RequestMiddleware(get_response=None)
#     request = request.thread_local.current_request
#     '''
#     if users login for the first time then a new User session object will be created.
#     '''
#     Session.objects.filter(user=user).delete()

#     # save current sesstion
#     request.session.save()

#     try:
#         mail_context = render_to_string('', {'user': user})
#         email = EmailMessage(
#             subject="Critical Security Alert",
#             body=mail_context,
#             from_email=settings.EMAIL_HOST_USER,
#             to=[user.email],
#             reply_to=["support@example.com"]  # <- your support email
#         )
#         email.content_subtype = "HTML"
#         EmailThread(email).start()
#         print("Email sent")
#     except Exception as error:
#         print(error)

#     # user_session = User.objects.get_or_create(user=user):
#     # if not user_session[1]:

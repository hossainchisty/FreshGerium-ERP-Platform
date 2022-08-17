from django.conf import settings
from django.core.mail import EmailMessage
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from expense.models import Expense
from utils.email_thread import EmailThread


@receiver(post_save, sender=Expense)
def send_alert(sender, instance, created, **kwargs):
    ''' Alert For Expense Claims '''
    email_template_name = "expense/pdf/email/expense_alert.html"
    email_context = {
        'expense_amount': instance.amount,
        'date': instance.date,
        'expense_type': instance.expense_type,
        'email': instance.user.email,
    }
    body = render_to_string(email_template_name, email_context)
    email = EmailMessage(
        subject="Expense Alert",
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[instance.user.email],
        reply_to=["freshdesk.support@gmail.com"]  # <- your support email
    )
    email.content_subtype = "HTML"
    with transaction.atomic():
        # If something went wrong/fails
        # The database will perform a rollback by itself.
        EmailThread(email).start()

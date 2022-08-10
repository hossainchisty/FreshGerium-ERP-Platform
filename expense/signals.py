from authenticator.models import User
from django.core.signals import request_finished, request_started
from django.db.models.signals import post_save
from django.dispatch import receiver
from expense.models import Expense


# TODO: Send notification/email to the accountant when expense will be created.
@receiver(post_save, sender=Expense)
def send_alert(sender, instance, created, **kwargs):
    print(f'Expense created Date: {instance.date}, Amount: {instance.expense_type}')


@receiver(request_started)
def mystarter(sender, **kwargs):
    print('Request Started!')


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print('Request Finished!')

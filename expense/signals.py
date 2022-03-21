from notifications.signals import notify

from authenticator.models import User
from django.db.models.signals import post_save
from expense.models import Expense

# TODO: Send notification to the accountant when expense will be created.
# def my_handler(sender, instance, created, **kwargs):
#     notify.send(instance, verb='was saved')
#     user = User.objects.get(id=1)
#     notify.send(user, recipient=user[0], verb='Added a new expense')


# post_save.connect(my_handler, sender=Expense)

from django.db import transaction
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from sales.models import Sale


@receiver(post_save, sender=Sale)
def discount(sender, instance, created, **kwargs):
    ''' Sales discount calculation '''
    with transaction.atomic():
        if instance.discount != 0:
            # Discount calculate Formula: original_price - (original_price * discount / 100)
            discounted_price = instance.total - (instance.total * instance.discount / 100)
            Sale.objects.filter(id=instance.id).update(total=discounted_price)


@receiver(post_save, sender=Sale)
def due(sender, instance, created, **kwargs):
    ''' Sales due calculation '''
    with transaction.atomic():
        due_amount = Sale.objects.filter(id=instance.id).aggregate(Sum('due'))['due__sum']
        total_amount = Sale.objects.filter(id=instance.id).aggregate(Sum('total'))['total__sum']
        payable_amount = due_amount + total_amount
        Sale.objects.filter(id=instance.id).update(total=payable_amount)

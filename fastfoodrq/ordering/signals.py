from django.db.models.signals import post_save
from django.dispatch import receiver
from fastfoodrq.ordering.models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_total(sender, instance, created, **kwargs):
        instance.refresh_price()

from django.db.models.signals import post_save
from django.dispatch import receiver
from fastfoodrq.ordering.models import (
    OrderItem,
    Order,
    Tab,
)


@receiver(post_save, sender=OrderItem)
def update_total_order_item(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_save, sender=Order)
def update_total_tab(sender, instance, created, **kwargs):
    instance.tab.update_total()

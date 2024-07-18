from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Actor, Movies


@receiver(post_save, sender=Actor)
def actor_saved(sender, instance, created, **kwargs):
    if created:
        print(f"Actor created: {instance.name}")
    else:
        print(f"Actor update: {instance.name}")

@receiver(post_delete, sender=Actor)
def actor_deleted(sender, instance, **kwargs):
    print(f"Actor deleted: {instance.name}")
    
@receiver(post_save, sender=Movies)
def actor_saved(sender, instance, created, **kwargs):
    if created:
        print(f"Movies created: {instance.title}")
    else:
        print(f"Movies update: {instance.title}")


@receiver(post_delete, sender=Movies)
def actor_deleted(sender, instance, **kwargs):
    print(f"Movies deleted: {instance.title}")
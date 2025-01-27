# Imports
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Feature



# receiver - function which will be connected to this signal        
# Pre-delete signal
@receiver(pre_delete, sender=Feature)
def pre_delete_post(sender, instance, **kwargs):
    if instance.pk:
        picture = Feature.objects.get(pk=instance.pk).profile_picture
        picture.delete(save=False)
        
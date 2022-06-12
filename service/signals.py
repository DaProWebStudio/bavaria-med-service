from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Service, ServiceLetter

@receiver(post_save, sender=Service)
def save_letter(sender, instance, **kwargs):
    if not instance.letterServices.all():
        letter, created = ServiceLetter.objects.get_or_create(letter=instance.get_letter(), 
                                                             defaults={'letter': instance.get_letter()})
        letter.services.add(instance)
        letter.save()
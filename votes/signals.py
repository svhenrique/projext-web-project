from .models import CamaraVoto

from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=CamaraVoto, dispatch_uid='slug_camara')
def camara_pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.nome)


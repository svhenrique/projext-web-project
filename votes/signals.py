from .models import CamaraVoto

from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.core.signals import request_started
from django.dispatch import receiver

import datetime
import pytz

@receiver(request_started, dispatch_uid='att_camaras')
def atualizar_camaras(sender, environ, **kwargs):
    """
    - Serve para verificar e atualizar, a cada request, se o tempo de uma camara já se
    encerrou, mudando seu estado de ativo (True) pra não ativo (False).
    - Explicando sobre timezone em python e em como lidar com naive datetime e aware datetime:
        - https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python
    """

    camaras = CamaraVoto.objects.all()
    for camara in camaras:

        termino = camara.termino
        agora = pytz.timezone("UTC").localize(datetime.datetime.now())

        if termino < agora:
            camara.ativo = False
            camara.save()

@receiver(pre_save, sender=CamaraVoto, dispatch_uid='slug_camara')
def camara_pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.nome)


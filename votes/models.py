import uuid

from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify

from django.dispatch import receiver
from django.core.signals import request_started

import datetime
import pytz

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):

    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class CamaraVoto(Base):

    nome = models.CharField('Nome da Camara de Votos', max_length=30, unique=True)
    inicio = models.DateTimeField('Inicio')
    termino = models.DateTimeField('Termino')
    slug = models.SlugField('Slug', max_length=50, blank=True, editable=False)

    def __str__(self):
        return self.nome

class Objeto(models.Model):

    camara = models.ForeignKey(CamaraVoto, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('Imagem', default="/static/img/blank-profile.png", upload_to=get_file_path,
                    variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})
    votos = models.IntegerField('Votos', default=0)

@receiver(request_started)
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

@receiver(signals.pre_save, sender=CamaraVoto)
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


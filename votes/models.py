import uuid

from django.db import models
from stdimage.models import StdImageField

import datetime
import pytz

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class CamaraManager(models.Manager):
    """
        Manager criado para verificação de validade de instâncias
        cada vez que uma query é feita.
        Deve ser aplicado com os objetos de CamaraVoto.
    """

    def get_queryset(self):
        """
            Método sobreposto para, antes de retornar a lista solicitada,
            atualizar a validade dos objetos de CamaraVoto
        """
        objetos = super().get_queryset()

        for objeto in objetos:
            objeto.atualizar_validade()

        return objetos

    def get_querybypk(self, pk):
        """
            Método criado para, ao solicitar um query por pk, atualizar a validade.
            dos objetos de CamaraVoto.
        """
        objeto = self.get(pk=pk)
        objeto.atualizar_validade()

        return objeto


class Base(models.Model):

    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class CamaraVoto(Base):

    objects = CamaraManager()

    nome = models.CharField('Nome da Camara de Votos', max_length=30, unique=True)
    inicio = models.DateTimeField('Inicio')
    termino = models.DateTimeField('Termino')
    slug = models.SlugField('Slug', max_length=50, blank=True, editable=False)

    def __str__(self):
        return self.nome

    def atualizar_validade(self):

        termino = self.termino
        agora = pytz.timezone("UTC").localize(datetime.datetime.now())

        if termino < agora:
            self.ativo = False
            self.save()


class Objeto(models.Model):

    camara = models.ForeignKey(CamaraVoto, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('Imagem', default="/static/img/blank-profile.png", upload_to=get_file_path,
                    variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})
    votos = models.IntegerField('Votos', default=0)


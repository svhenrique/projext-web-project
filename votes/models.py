import uuid

from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify

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


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=CamaraVoto)
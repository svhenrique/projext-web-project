import uuid

from django.db import models
from stdimage.models import StdImageField

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

class Tempo(models.Model):

    inicio = models.DateTimeField('Inicio')
    termino = models.DateTimeField('Termino')

class CamaraVoto(Base):
    # ver pq o tempo não é deletado quando a camara é deletada
    tempo = models.OneToOneField(Tempo, verbose_name='Tempo', on_delete=models.CASCADE, unique=True)


class Objeto(models.Model):

    camara = models.ForeignKey(CamaraVoto, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=10)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('Imagem', default="/static/img/blank-profile.png", upload_to=get_file_path,
                    variations={'thumb': {'width': 400, 'height': 400, 'crop': True}})


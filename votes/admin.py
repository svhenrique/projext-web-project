from django.contrib import admin
from .models import Objeto, CamaraVoto

class ObjetosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'votos')

class CamaraVotoAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'nome', 'slug', 'criado', 'modificado', 'inicio', 'termino')

admin.site.register(Objeto, ObjetosAdmin)
admin.site.register(CamaraVoto, CamaraVotoAdmin)
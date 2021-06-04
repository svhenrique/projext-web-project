from django.contrib import admin
from .models import Objeto, Tempo, CamaraVoto

class ObjetosAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class CamaraVotoAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'criado', 'modificado', 'tempo')

class TempoAdmin(admin.ModelAdmin):
    list_display = ('inicio', 'termino')

admin.site.register(Objeto, ObjetosAdmin)
admin.site.register(Tempo, TempoAdmin)
admin.site.register(CamaraVoto, CamaraVotoAdmin)
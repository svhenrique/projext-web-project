from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .models import CamaraVoto

class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        camaras = CamaraVoto.objects.all()
        camaras_data = []

        for camara in camaras:

            nome = camara.nome
            ativo = camara.ativo
            inicio = camara.inicio
            termino = camara.termino
            slug = camara.slug

            camara_data = {
                'nome': nome,
                'ativo': ativo,
                'inicio': inicio,
                'termino': termino,
                'slug': slug
            }

            camaras_data.append(camara_data)

        kwargs['camaras_data'] = camaras_data

        return super().get_context_data(**kwargs)
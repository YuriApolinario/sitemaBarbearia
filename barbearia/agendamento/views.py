from django.shortcuts import render
from django.views.generic import TemplateView

class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "index.html"

# Página "Sobre"
class SobreView(TemplateView):
    template_name = "sobre.html"

# Página de contato
class ContatoView(TemplateView):
    template_name = "contato.html"

# Página de curriculo
class CurriculoView(TemplateView):
    template_name = "curriculo.html"

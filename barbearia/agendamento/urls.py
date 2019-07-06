from django.urls import path
from .views import *


urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo")
    path('formulario/', CurriculoView.as_view(), name="formulario")

]

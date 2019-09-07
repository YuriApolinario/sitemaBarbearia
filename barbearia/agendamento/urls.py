from django.urls import path
from .views import *


urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('contato/', ContatoView.as_view(), name="contato"),
    path('curriculo/', CurriculoView.as_view(), name="curriculo"),
    path('formulario/', FormularioView.as_view(), name="formulario"),

        # URLS de Estado
    path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name="editar-estado"),
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name="excluir-estado"),
    path('listar/estados/', EstadoList.as_view(), name="listar-estados"),

    # URLS de Cidade
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name="editar-cidade"),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name="excluir-cidade"),
    path('listar/cidade/', CidadeList.as_view(), name="listar-cidades"),



    # URLS de cliente
    path('cadastrar/cliente/', ClienteCreate.as_view(), name="cadastrar-cliente"),
    path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name="editar-cliente"),
    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name="excluir-cliente"),
    path('listar/cliente/', ClienteList.as_view(), name="listar-clientes"),

    # URLS de barbeiro
    path('cadastrar/barbeiro/', BarbeiroCreate.as_view(), name="cadastrar-barbeiro"),
    path('editar/barbeiro/<int:pk>/', BarbeiroUpdate.as_view(), name="editar-barbeiro"),
    path('excluir/barbeiro/<int:pk>/', BarbeiroDelete.as_view(), name="excluir-barbeiro"),
    path('listar/barbeiro/', BarbeiroList.as_view(), name="listar-barbeiros"),
    
    # URLS de agenda
    path('cadastrar/agenda/', AgendamentoCreate.as_view(),name="cadastrar-agenda"),
    path('editar/agenda/<int:pk>/',AgendamentoUpdate.as_view(), name="editar-agenda"),
    path('excluir/agenda/<int:pk>/',AgendamentoDelete.as_view(), name="excluir-agenda"),
    path('listas/agenda/', AgendamentoList.as_view(), name="listar-agendas"),
    
    # URLS de caixa
    path('cadastrar/caixa/', CaixaCreate.as_view(),name="cadastrar-caixa"),
    path('editar/barbeiro/<int:pk>/',CaixaUpdate.as_view(), name="editar-caixa"),
    path('listas/caixa/', CaixaList.as_view(), name="listar-caixas"),
    
    

]

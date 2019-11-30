from django.shortcuts import render

from braces.views import GroupRequiredMixin

# Importa todas as classes do models.py

# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

from .models import Barbeiro, Cidade, Estado, Cliente, Caixa, Agendamento
# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView

#impota o Mixin para obrigar logar
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)


class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "agendamento/index.html"

# Página "Sobre"


class SobreView(TemplateView):
    template_name = "agendamento/sobre.html"

# Página de contato


class ContatoView(TemplateView):
    template_name = "agendamento/contato.html"

# Página de Currículo


class CurriculoView(TemplateView):
    template_name = "agendamento/curriculo.html"

#pagina de contato

class FormularioView(TemplateView):
    template_name = "agendamento/formulario.html"
##################### INSERIR ######################


class EstadoCreate(LoginRequiredMixin, CreateView):
    group_required = u"Barbeiro"
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "agendamento/formulario.html"
    # Pra onde redirecionar o usuário depois de inserir um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")
    # Quais campos devem aparecer no formulário?
    fields = ['sigla', 'nome']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoCreate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    group_required = u"Barbeiro"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context




class ClienteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Cliente
    group_required = u"Barbeiro"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-clientes")
    fields = ['nome','cpf','telefone']

    def get_context_data(self, *args, **kwargs):
        context = super(ClienteCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cdastro de clientes" 
        context['botao'] = "cadastrar"
        context['classeBotao'] = "btn-primary"
        return context
    

class BarbeiroCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Barbeiro
    group_required = u"Barbeiro"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-barbeiros")
    fields = ['nome','especialidade']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(BarbeiroCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Barbeiros"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class CaixaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Caixa
    group_required = u"Barbeiro"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("movimento-caixa")
    fields = ['entrada','saida', 'FormaPagamento']
    
    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CaixaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Movimento Financeiro"
        context['botao'] = "Venda"
        context['classeBotao'] = "btn-primary"
        return context
    
class AgendamentoCreate(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = Agendamento
    group_required = u"Barbeiro"
    template_name = "agendamento/formulario.html"
    succes_url = reverse_lazy("movimento-caixa")
    fields=['data','hora','servico']
    
    def get_context_data(self,*args, **kwargs):
        context = super(AgendamentoCreate, self ).get_context_data(*args, **kwargs)
        context['titulo'] = "Agenda"
        context['botao'] = "agendar"
        context['classeBotao'] = "btn-primary"
        return context

        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

##################### EDITAR ######################


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "agendamento/formulario.html"
    # Pra onde redirecionar o usuário depois de editar um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")
    # Quais campos devem aparecer no formulário?
    fields = ['sigla', 'nome']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoUpdate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Editar cadastro de Estado"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"

        # Devolve/envia o context para seu comportamento padrão
        return context


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado', 'descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CidadeUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Cidade"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class CaixaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Caixa
    group_required = u"Administrador"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-caixas")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CaixaUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar caixa"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class AgendamentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Agendamento
    group_required = u"Barbeiro"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-agendamento")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(AgendamentoUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Agenda"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context



class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-clientes")
    fields = ['ome, telefone, cpf']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(ClienteUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de clientes"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"

        return context


class BarbeiroUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Barbeiro
    group_required = u"Adminstrador"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-Barbeiro")
    fields = ['nome','especialidade']
   
    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(BarbeiroUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Barbeiro"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-primary"
        return context


##################### Excluir ######################


class EstadoDelete(LoginRequiredMixin, DeleteView):
    # Define qual o modelo pra essa classe vai criar o form
    model = Estado
    # Qual o html que será utilizado?
    template_name = "agendamento/formulario.html"
    # Pra onde redirecionar o usuário depois de excluir um registro. Informe o nome da url
    success_url = reverse_lazy("listar-estados")

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(EstadoDelete, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        # Devolve/envia o context para seu comportamento padrão
        return context

class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-cidades")

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class ClienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Cliente
    group_required = u"Adminstrador"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-clientes")

    def get_context_data(self, *args, **kwargs):
        context = super(ClienteDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class BarbeiroDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Barbeiro
    group_required = u"Adminstrador"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-barbeiros")

    def get_context_data(self, *args, **kwargs):
        context = super(BarbeiroDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context


class AgendamentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Agendamento
    group_required = u"Adminstrador"
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-agendamento")

    def get_context_data(self, *args, **kwargs):
        context = super(AgendamentoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context
    
    

##################### Listar ######################

# Vai gerar uma tela com uma lista de estados


class EstadoList(LoginRequiredMixin, ListView):
    # Inform qual o modelo
    model = Estado
    # E o template
    template_name = "agendamento/listas/listar_estado.html"

class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = "agendamento/listas/listar_cidade.html"


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "agendamento/listas/listar_clientes.html"

class BarbeiroList(LoginRequiredMixin, ListView):
    model = Barbeiro
    template_name = "agendamento/listas/listar_barbeiro.html"
    
class AgendamentoList(LoginRequiredMixin, ListView):
    model = Agendamento
    template_name = "agendamento/listas/listar_agendamento.html"



class CaixaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Barbeiro
    group_required = u"Adminstrador"
    template_name = "agendamento/listas/listar_caixa.html"

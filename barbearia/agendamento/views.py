from django.shortcuts import render

# Importa todas as classes do models.py

# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

from .models import Pessoa, Barbeiro, Cidade, Estado, Cliente 
# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView

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

class EstadoCreate(CreateView):
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


class CidadeCreate(CreateView):
    model = Cidade
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-cidades")
    fields = ['nome', 'estado', 'descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(CidadeCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Cidades"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

class PessoaCreate(CreateView):
    model = Pessoa
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-pessoas")
    fields = ['nome','cpf']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(PessoaCreate,self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Pessoas" 
        context['botao'] = "cadastrar"
        context['classBotao'] = "btn-primary"
        return context
    
class ClienteCreate(CreateView):
    model = Cliente
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-clientes")
    fields = ['descricao']

    def get_context_data(self, *args, **kwargs):
        context = super(ClienteCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cdastro de clientes" 
        context['botao'] = "cadastrar"
        context['classBotao'] = "btn-primary"
        return context
    

class BarbeiroCreate(CreateView):
    model = Barbeiro
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-barbeiros")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(BarbeiroCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Barbeiros"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context




##################### EDITAR ######################


class EstadoUpdate(UpdateView):
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


class CidadeUpdate(UpdateView):
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


class PessoaUpdate(UpdateView):
    model = Pessoa
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-pessoas")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(TipoUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de pessoa"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-clientes")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(RacaUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de clientes"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class BarbeiroUpdate(UpdateView):
    model = Barbeiro
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-Barbeiro")
   
    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(AnimalUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Barbeiro"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-primary"
        return context

##################### Excluir ######################


class EstadoDelete(DeleteView):
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

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-cidades")

    def get_context_data(self, *args, **kwargs):
        context = super(CidadeDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-pessoas")

    def get_context_data(self, *args, **kwargs):
        context = super(TipoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-clientes")

    def get_context_data(self, *args, **kwargs):
        context = super(RacaDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class BarbeiroDelete(DeleteView):
    model = Barbeiro
    template_name = "agendamento/formulario.html"
    success_url = reverse_lazy("listar-barbeiros")

    def get_context_data(self, *args, **kwargs):
        context = super(AnimalDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

##################### Listar ######################

# Vai gerar uma tela com uma lista de estados


class EstadoList(ListView):
    # Inform qual o modelo
    model = Estado
    # E o template
    template_name = "agendamento/listas/list_estado.html"

class CidadeList(ListView):
    model = Cidade
    template_name = "agendamento/listas/list_cidade.html"

class PessoaList(ListView):
    model = Pessoa
    template_name = "agendamento/listas/listar_pessoas.html"

class ClienteList(ListView):
    model = Cliente
    template_name = "agendamento/listas/listar_clientes.html"

class BarbeiroList(ListView):
    model = Barbeiro
    template_name = "agendamento/listas/listar_barbeiro.html"

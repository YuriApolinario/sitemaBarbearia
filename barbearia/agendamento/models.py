from django.db import models

#importar modelo user
from django.contrib.auth.models import User


# Create your models here.


class Estado(models.Model):
    # nome_do_atributo = models.Tipo(configuração)
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=50)
    # Como se fosse toString e self = this
    def __str__(self):
        return self.sigla + ' - ' + self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descricao = models.TextField(
        blank=True, null=True, verbose_name="Descrição",
        help_text="Espaço para colocar qualquer informação."
    )

    def __str__(self):
        return self.nome + '/' + self.estado.sigla

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=12)

  

class Barbeiro(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=50)
   
   
class Caixa(models.Model):
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.PROTECT)
    entrada = models.CharField(max_length=5) 
    saida = models.CharField(max_length=50)
    formaPagamento = models.CharField(max_length=50)
    
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
class Agendamento(models.Model):
    data = models.CharField(max_length=11)
    hora = models.CharField(max_length=4)
    servico = models.CharField(max_length=10)
    
    
    
    

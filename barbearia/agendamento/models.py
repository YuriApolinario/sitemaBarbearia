from django.db import models

# Create your models here.

class  Estado(models.Model):
    sigla = models.CharField(max_lenght=2)
    nome = models.CharField(max_lenght=50 )

    def __str__(self):
        return self.sigla + ' - ' + self.nome
class Cidade(models.model):
    nome = models.charField(max_lenght=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)


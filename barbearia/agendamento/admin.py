from django.contrib import admin
from .models import Barbeiro, Cidade, Estado, Cliente, Pessoa

# Register your models here.
admin.site.register(Barbeiro)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Cliente)
admin.site.register(Pessoa)

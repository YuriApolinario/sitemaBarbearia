from django.contrib import admin
from .models import Barbeiro, Cidade, Estado, Agendamento, Caixa

# Register your models here.
admin.site.register(Barbeiro)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Agendamento)
admin.site.register(Caixa)


# admin.site.register(Cliente)

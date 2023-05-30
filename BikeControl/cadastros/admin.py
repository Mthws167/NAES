from django.contrib import admin
from .models import Administrador, Empresa, Cliente, Marca, Modelo, Moto, Venda, Carrinho

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Moto)
admin.site.register(Venda)
admin.site.register(Carrinho)


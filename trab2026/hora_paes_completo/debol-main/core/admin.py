from django.contrib import admin

from .models import (
    Categoria,
    Produto,
    Cliente,
    Funcionario,
    Venda,
    ItemVenda
)

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Venda)
admin.site.register(ItemVenda)
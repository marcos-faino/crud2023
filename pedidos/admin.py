from django.contrib import admin

from pedidos.models import Endereco, Cliente, Pedido, Produto

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['rua', 'numero', 'bairro']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'endereco']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'data_pedido', 'valor']
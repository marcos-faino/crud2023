from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from pedidos import models


class IndexView(TemplateView):
    template_name = 'index.html'


class ListarProdutosView(ListView):
    model = models.Produto
    template_name = 'loja/listarprodutos.html'
    context_object_name = 'produtos'


class CadastrarProdutoView(CreateView):
    model = models.Produto
    template_name = 'loja/formprodutos.html'
    fields = ['nome', 'descricao', 'valor']
    success_url = reverse_lazy('listarprod')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['op'] = 's'
        return contexto


class AtualizarProdutoView(UpdateView):
    model = models.Produto
    template_name = 'loja/formprodutos.html'
    fields = ['nome', 'descricao', 'valor']
    success_url = reverse_lazy('listarprod')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['op'] = 'a'
        return contexto


class ExcluirProdutoView(DeleteView):
    model = models.Produto
    template_name = 'loja/excluirproduto.html'
    success_url = reverse_lazy('listarprod')
    context_object_name = 'produto'



class ListarClientesView(ListView):
    model = models.Cliente
    template_name = 'loja/listarclientes.html'
    context_object_name = 'clientes'


class CadastrarClienteView(CreateView):
    model = models.Cliente
    template_name = 'loja/formclientes.html'
    fields = ['nome', 'data_nascimento', 'email', 'sexo', 'endereco']
    success_url = reverse_lazy('listarcli')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['op'] = 'c'
        return contexto


class AtualizarClienteView(UpdateView):
    model = models.Cliente
    template_name = 'loja/formclientes.html'
    fields = ['nome', 'data_nascimento', 'email', 'sexo', 'endereco']
    success_url = reverse_lazy('listarcli')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['op'] = 'a'
        return contexto


class ExcluirClienteView(DeleteView):
    model = models.Cliente
    template_name = 'loja/excluircliente.html'
    success_url = reverse_lazy('listarcli')
    context_object_name = 'cliente'


class CadastrarEnderecoView(CreateView):
    model = models.Endereco
    template_name = 'loja/formenderecos.html'
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade']
    success_url = reverse_lazy('addcliente')


class ListarPedidosView(ListView):
    model = models.Pedido
    template_name = 'loja/listarpedidos.html'
    context_object_name = 'pedidos'


class CadastrarPedidoView(CreateView):
    model = models.Pedido
    template_name = 'loja/formpedidos.html'
    fields = ['cliente', 'valor', 'status', 'produtos']
    success_url = reverse_lazy('listarpedidos')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['op'] = 's'
        return contexto


class AtualizarPedidoView(UpdateView):
    model = models.Pedido
    template_name = 'loja/formpedidos.html'
    fields = ['cliente', 'valor', 'status', 'produtos']
    success_url = reverse_lazy('listarpedidos')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['op'] = 'a'
        return contexto


class ExcluirPedidoView(DeleteView):
    model = models.Pedido
    template_name = 'loja/excluirpedido.html'
    success_url = reverse_lazy('listarpedidos')
    context_object_name = 'pedido'

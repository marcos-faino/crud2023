from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

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
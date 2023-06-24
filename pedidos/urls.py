from django.urls import path
from pedidos import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('produtos/', views.ListarProdutosView.as_view(), name='listarprod'),
    path('addproduto/', views.CadastrarProdutoView.as_view(), name='cadproduto'),
    path('atualizarproduto/<int:pk>', views.AtualizarProdutoView.as_view(), name='updateproduto'),
    path('excluirproduto/<int:pk>', views.ExcluirProdutoView.as_view(), name='excluirproduto'),
    path('clientes/', views.ListarClientesView.as_view(), name='listarcli'),
    path('cadatualcliente/', views.CadastrarClienteView.as_view(), name='addcliente'),
    path('cadatualcliente/<int:pk>', views.AtualizarClienteView.as_view(), name='atualcliente'),
    path('excluircliente/<int:pk>', views.ExcluirClienteView.as_view(), name='excluircliente'),
    path('cadendereco/<str:nome>/<str:data_nasc>/<str:email>/<str:sexo>', views.CadastrarEnderecoView.as_view(), name='cadendereco'),
    path('cadendereco/', views.CadastrarEnderecoView.as_view(), name='cadendereco'),
    path('pedidos/', views.ListarPedidosView.as_view(), name='listarpedidos'),
    path('addpedido/', views.CadastrarPedidoView.as_view(), name='cadpedido'),
    path('atualizarpedido/<int:pk>', views.AtualizarPedidoView.as_view(), name='updatepedido'),
    path('excluirpedido/<int:pk>', views.ExcluirPedidoView.as_view(), name='excluirpedido'),
]
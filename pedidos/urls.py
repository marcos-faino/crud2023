from django.urls import path
from pedidos import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('produtos/', views.ListarProdutosView.as_view(), name='listarprod'),
    path('addproduto/', views.CadastrarProdutoView.as_view(), name='cadproduto'),
    path('atualizarproduto/<int:pk>', views.AtualizarProdutoView.as_view(), name='updateproduto'),
    path('excluirproduto/<int:pk>', views.ExcluirProdutoView.as_view(), name='excluirproduto'),
]
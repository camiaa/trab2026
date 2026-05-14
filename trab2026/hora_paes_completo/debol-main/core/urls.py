from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('produtos-site/', ProdutosView.as_view(), name='produtos_site'),
    path('diagrama/', DiagramaView.as_view(), name='diagrama'),
    path('lista/', ListaProdutosView.as_view(), name='lista_produtos'),
    path('criar/', CriarProdutoView.as_view(), name='criar_produto'),
    path('editar/<int:id>/', EditarProdutoView.as_view(), name='editar_produto'),
    path('excluir/<int:id>/', ExcluirProdutoView.as_view(), name='excluir_produto'),
    path('vender/<int:id>/', VenderProdutoView.as_view(), name='vender_produto'),
]
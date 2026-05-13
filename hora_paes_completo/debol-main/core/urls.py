from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('produtos-site/', views.produtos, name='produtos_site'),

    path('produtos/', views.lista_produtos, name='lista_produtos'),

    path('produtos/novo/', views.criar_produto, name='criar_produto'),

    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),

    path('vender/<int:id>/', views.vender_produto, name='vender_produto'),

    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
]
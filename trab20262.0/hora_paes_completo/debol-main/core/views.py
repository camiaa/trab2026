from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Produto



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()[:3]
        return context



class ProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'



class DiagramaView(TemplateView):
    template_name = 'diagrama.html'



class ListaProdutosView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'lista_produtos.html'
    context_object_name = 'produtos'



class CriarProdutoView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'criar_produto.html'
    fields = ['nome', 'preco', 'quantidade_estoque', 'descricao']
    success_url = reverse_lazy('lista_produtos')



class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'



class EditarProdutoView(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'editar_produto.html'
    fields = ['nome', 'preco', 'quantidade_estoque', 'descricao']
    success_url = reverse_lazy('home')



class ExcluirProdutoView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('lista_produtos')



class VenderProdutoView(LoginRequiredMixin, DetailView):
    model = Produto

    def get(self, request, *args, **kwargs):
        produto = self.get_object()

        if produto.quantidade_estoque > 0:
            produto.quantidade_estoque -= 1
            produto.save()

        return redirect('produtos_site')
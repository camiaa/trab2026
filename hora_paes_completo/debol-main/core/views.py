from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from django.contrib.auth.decorators import user_passes_test


def home(request):
    produtos = Produto.objects.all()[:3]
    return render(request, 'home.html', {'produtos': produtos})


def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})


@login_required
def criar_produto(request):
    if request.method == 'POST':
        Produto.objects.create(
            nome=request.POST['nome'],
            preco=request.POST['preco'],
            quantidade_estoque=request.POST['estoque'],
            descricao=request.POST['descricao']
        )
        return redirect('lista_produtos')

    return render(request, 'criar_produto.html')


@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos')


@login_required
def vender_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if produto.quantidade_estoque > 0:
        produto.quantidade_estoque -= 1
        produto.save()

    return redirect('produtos_site')


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.preco = request.POST['preco']
        produto.quantidade_estoque = request.POST['estoque']
        produto.descricao = request.POST['descricao']

        produto.save()

        return redirect('home')

    return render(request, 'editar_produto.html', {
        'produto': produto
    })
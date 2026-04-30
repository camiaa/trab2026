from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Produto




class Index(TemplateView):
    template_name = "website/inicio.html"

class Sobre(TemplateView):
    template_name = "website/sobre.html"

class Contato(TemplateView):
    template_name = "website/contato.html"

    def home(request):
        produtos = Produto.objects.all()[:3]
        return render(request, 'home.html', {'produtos': produtos})

    def produtos(request):
        lista = Produto.objects.all()
        return render(request, 'Produto.html', {'produtos': lista})

    def detalhe(request, id):
        produto = get_object_or_404(Produto, id=id)
        return render(request, 'detalhe.html', {'produto': produto})
    
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def produtos(request):
    return render(request, 'produtos.html')

def detalhe(request):
    return render(request, 'detalhe.html')
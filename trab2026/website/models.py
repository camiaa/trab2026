from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.URLField()
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome

# Create your models here.

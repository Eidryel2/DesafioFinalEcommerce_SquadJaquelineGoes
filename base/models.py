from django.db import models
from base.classes import Item

class Produtos(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=255, null=False)
    imgUrl = models.CharField(max_length=1000,null=False)
    preco = models.FloatField(null=False)
    qtdEstoque = models.IntegerField(null=False)

class Carrinho(models.Model):
    produtos = models.JSONField()

class Pedidos(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    produtos = models.JSONField()

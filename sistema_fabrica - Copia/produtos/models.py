from django.db import models
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from .models import Produto

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

@login_required 
def listar_produtos (request):
    produtos = Produto.objects.all() 
    return render (request, 'listar_produtos.html', {'produtos': produtos}) 
from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from django.http import JsonResponse
from .schemas import Produto
from .models import Produtos as ModelProdutos

produtos_router = Router()

@produtos_router.get('/',response=List[Produto])
def home_produtos(request):
    produtos =ModelProdutos.objects.all()
    return produtos

@produtos_router.get('produto/{id_produto}/',response=Produto)
def get_produto(request,id_produto:int):
    produto = get_object_or_404(ModelProdutos, id =id_produto)
    return produto
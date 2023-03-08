from ninja import Router
from django.http import JsonResponse
from .schemas import Produto
from .models import Produtos as ModelProdutos

produtos_router = Router()

@produtos_router.get('/')
def home_produtos(request):
    
    return JsonResponse({'home':1})

@produtos_router.get('produto/')
def get_produto(request):
    return JsonResponse({'produto':2})
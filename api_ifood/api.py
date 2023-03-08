from ninja import NinjaAPI
from Produtos.api import  produtos_router


api = NinjaAPI()

api.add_router('/produtos',produtos_router)
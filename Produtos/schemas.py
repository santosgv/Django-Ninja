from ninja import Schema,ModelSchema
from typing import List,Dict
from .models import Produtos

class Produto(ModelSchema):
    class Config:
        model = Produtos
        model_fields= "__all__"
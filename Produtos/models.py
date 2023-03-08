from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=20)
    preco = models.FloatField()
    src = models.ImageField(upload_to='post_img')
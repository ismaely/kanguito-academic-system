from django.db import models
from pessoa.models import Pessoa
# Create your models here.

class Aluno(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    #numero_estudante= models.CharField(max_length=30, blank=True, null=True, default="NULL")
    media_conclusao = models.CharField(max_length=3, blank=True, null=True)
    instituicao_origem = models.CharField(max_length=120, blank=True, null=True,default="")
    data_registro = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id
    class Meta:
        order_with_respect_to = 'pessoa'
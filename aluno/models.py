from django.db import models
from pessoa.models import Pessoa
from config.models import Opcao_Matricula, Periodo, Tremestre,Ano
from curso.models import Curso
# Create your models here.

class Aluno(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    numero_estudante= models.CharField(max_length=30, blank=True, null=True, default="")
    media_conclusao = models.CharField(max_length=2, blank=True, null=True)
    instituicao_origem = models.CharField(max_length=120, blank=True, null=True,default="")
    data_registro = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id
    class Meta:
        order_with_respect_to = 'pessoa'



class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    opcao_matricula = models.ForeignKey(Opcao_Matricula, on_delete=models.CASCADE, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    tremestre = models.ForeignKey(Tremestre, on_delete=models.CASCADE, parent_link=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, parent_link=True)
    data = models.DateField(max_length=20)
    nota_exame = models.CharField(max_length=2, null=True,blank=True, default=" ")

    def __str__ (self):
        return self.id

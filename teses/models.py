from django.db import models
from curso.models import Curso

# Create your models here.


# modelo que reprsenta o tema para defesa
"""class Tema_Tcc(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True, parent_link=True)
    tema = models.CharField(max_length=100, null=True, default="")
    opcao = models.CharField(max_length=20, choices=INDIVIAL_GRUPO)
    #numero_alunos = models.CharField(max_length=3, null=True, blank=True, default="")
    situacao = models.CharField(max_length=30, null=True, blank=True, default="Aprovado")
    data_entrada = models.DateField()
    descricao = models.TextField(max_length=1900, null=True, blank=True, default="")

    class Meta:
        ordering = ['situacao']
    def __str__ (self):
        return self.id
"""
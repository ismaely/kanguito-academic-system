from django.contrib import admin
from django.db import models
from django.utils import timezone
from pessoa.models import Pessoa
from config.models import Opcao_Matricula, Periodo, Tremestre,Ano, Grau_academico
from curso.models import Curso
from docente.models import Orientador
from unidade_curricular.models import UnidadeCurricular_Curso
# Create your models here.


class Motivo_Reclamacao(models.Model):
    nome = models.CharField(max_length=50)
    opcao = models.CharField(max_length=160, blank=True, null=True)
    def __str__ (self):
        return "%s" % (self.nome)



class Aluno(models.Model):

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    grau_academico = models.ForeignKey(Grau_academico, on_delete=models.CASCADE, parent_link=True)
    numero_estudante= models.CharField(max_length=30, blank=True, null=True, default="")
    area_formacao = models.CharField(max_length=200, blank=True, null=True,default="")
    curso_frequentado = models.CharField(max_length=190)
    media_conclusao = models.CharField(max_length=2, blank=True, null=True)
    instituicao_origem = models.CharField(max_length=120)
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    @admin.display(ordering='-pessoa_nome')
    def __str__ (self):
        return self.id
    

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    opcao_matricula = models.ForeignKey(Opcao_Matricula, on_delete=models.CASCADE, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    tremestre = models.ForeignKey(Tremestre, on_delete=models.CASCADE, parent_link=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, parent_link=True)
    dataMatricula = models.DateField(default=timezone.now)
    nota_exame = models.CharField(max_length=2, null=True,blank=True, default=" ")
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id



class Reclamacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    motivo = models.ForeignKey(Motivo_Reclamacao, on_delete=models.CASCADE, parent_link=True)
    data_reclamacao = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=20, null=True, default="Em Analise")
    descricao = models.CharField(max_length=3000, null=True, default="")
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    @admin.display(ordering='-aluno')
    def __str__ (self):
        return self.id



class Confirmar_Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    tremestre = models.ForeignKey(Tremestre, on_delete=models.CASCADE, blank=True, null=True, parent_link=True)
    data_confirmacao = models.DateField(default=timezone.now)
    periodo = models.ForeignKey(Periodo, on_delete=models.SET_NULL, blank=True, null=True, parent_link=True)
    cadeiras_atraso = models.ManyToManyField(UnidadeCurricular_Curso,  blank=True, null=True)
    responsavel = models.CharField(max_length=190, blank=True, null=True)
    numero_recibo = models.CharField(max_length=15, blank=True, null=True)
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-aluno"]

    def __str__ (self):
        return self.id


"""class Orientacao_Tcc(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE, parent_link=True)
    data_candidatura = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=20, null=True, default="Em Analise")
    descricao = models.CharField(max_length=3000, null=True, default="")
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    @admin.display(ordering='-aluno')
    def __str__ (self):
        return self.id
"""
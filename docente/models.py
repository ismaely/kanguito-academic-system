from django.db import models
from django.utils import timezone
from pessoa.models import Pessoa
from config.models import Periodo, Ano, Tremestre
from unidade_curricular.models import UnidadeCurricular
from curso.models import Curso

# Create your models here.

class Docente_Grau_academico(models.Model):
    nome = models.CharField(max_length=50)
    opcao = models.CharField(max_length=160, blank=True, null=True)
    def __str__ (self):
        return "%s" % (self.nome)


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    opcao = models.CharField(max_length=160, blank=True, null=True)
    def __str__ (self):
        return "%s" % (self.nome)


class Estado_Docente(models.Model):
    nome = models.CharField(max_length=50)
    opcao = models.CharField(max_length=160, blank=True, null=True)
    def __str__ (self):
        return "%s" % (self.nome)


class Estado_Orientador(models.Model):
    nome = models.CharField(max_length=50)
    opcao = models.CharField(max_length=160, blank=True, null=True)
    def __str__ (self):
        return "%s" % (self.nome)

class Docente(models.Model):
    pessoa= models.ForeignKey(Pessoa, on_delete=models.CASCADE, parent_link=True)
    numero_docente= models.CharField(max_length=10, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, parent_link=True)
    grau_academico = models.ForeignKey(Docente_Grau_academico, on_delete=models.CASCADE, parent_link=True)
    estado= models.ForeignKey(Estado_Docente, on_delete=models.CASCADE, parent_link=True)
    data_registro = models.DateField(default=timezone.now)
    created = models.DateField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return 'Dr %s'  % (self.pessoa.nome)


class Orientador(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    data_limite = models.DateField(default=timezone.now)
    estado = models.ForeignKey(Estado_Orientador, on_delete=models.CASCADE, parent_link=True)
    numero_orientados = models.IntegerField(default=1)
    created = models.DateField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id


class Unidade_Curricular_Docente(models.Model):
    docente= models.ForeignKey(Docente, on_delete=models.CASCADE, parent_link=True)
    curso= models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    unidadeCurricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, parent_link=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, parent_link=True)
    estado = models.ForeignKey(Estado_Docente, on_delete=models.CASCADE, parent_link=True, default=1)
    nivel_academico = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    ano_letivo = models.CharField(max_length=190, default=timezone.now().year)
    tremestre = models.ForeignKey(Tremestre, on_delete=models.CASCADE, parent_link=True)
    data_registro = models.DateField(default=timezone.now)
    created = models.DateField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return '%d'  % (self.id)

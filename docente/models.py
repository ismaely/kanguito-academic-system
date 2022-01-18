from django.db import models
from django.utils import timezone
from pessoa.models import Pessoa

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
        return '%d'  % (self.id)

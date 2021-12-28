from django.db import models
from config.models import Pais, Provincia, Municipio, Genero, Estado_Civil, Documento_identificacao

# Create your models here. unique=True

class Dificiencia(models.Model):
    nome = models.CharField(max_length=4)
    def __str__ (self):
        return "%s" % (self.nome)

class Tipo_Dificiencia(models.Model):
    nome = models.CharField(max_length=200)
    duracao = models.CharField(max_length=400, null=True, default=" ")


class Pessoa(models.Model):
    nome = models.CharField(max_length=200,)
    nome_pai = models.CharField(max_length=200, blank=True, null=True, default="")
    nome_mae = models.CharField(max_length=200, blank=True, null=True, default="")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, parent_link=True, blank=True, null=True)
    data_nascimento=models.CharField(max_length=20)
    ndi = models.CharField(max_length=40)
    documento = models.ForeignKey(Documento_identificacao, on_delete=models.CASCADE, parent_link=True)
    estado_civil = models.ForeignKey(Estado_Civil, on_delete=models.CASCADE, parent_link=True)
    residencia = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True, default="")
    email = models.EmailField(max_length=190, blank=True, null=True, default="")
    dificiencia = models.ForeignKey(Dificiencia, on_delete=models.CASCADE, parent_link=True, blank=True, null=True)
    tipo_Dificiencia = models.ForeignKey(Tipo_Dificiencia, on_delete=models.CASCADE, parent_link=True, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, parent_link=True, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, parent_link=True,  blank=True, null=True, default="")
    nacionalidade = models.ForeignKey(Pais, on_delete=models.CASCADE, parent_link=True, default=6)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True, default="user.jpg")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.id

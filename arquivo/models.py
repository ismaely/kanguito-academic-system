from django.db import models
#from django.contrib import admin



class Tipologia(models.Model):
    nome = models.CharField(max_length=150)
    def __str__ (self):
        return "%s" % (self.nome)


class Categoria_Partilha(models.Model):
    nome = models.CharField(max_length=150)
    def __str__ (self):
        return "%s" % (self.nome)


# Create your models here.
class Arquivo(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=170, blank=True, null=True)
    numero_pagina = models.CharField(max_length=5, null=True, blank=True, default="")
    tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE, parent_link=True)
    partilha = models.ForeignKey(Categoria_Partilha, on_delete=models.SET_NULL, parent_link=True,  blank=True, null=True, default="")
    data = models.DateField()
    arquivo = models.FileField(upload_to="uploads/%Y/")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

   
    class Meta:
        ordering = ['titulo']
    def __str__ (self):
        return self.id

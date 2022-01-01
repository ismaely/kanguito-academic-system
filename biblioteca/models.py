from django.db import models

# Create your models here.
class Categoria_livro(models.Model):
    nome = models.CharField(max_length=100,null=True, blank=True, default="")
    class Meta:
        ordering = ['nome']
    def __str__ (self):
        return "%s" % (self.nome)


class Livro(models.Model):
    categoria = models.ForeignKey(Categoria_livro, on_delete=models.SET_NULL, blank=True, null=True, parent_link=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    numero_pagina = models.CharField(max_length=5, null=True, blank=True, default="")
    isbn = models.CharField(max_length=14, null=True, blank=True, default="")
    data_entrada = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['titulo']
    def __str__ (self):
        return self.id
        
        
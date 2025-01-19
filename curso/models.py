from django.db import models

# Create your models here.


class Curso(models.Model):
    nome = models.CharField(max_length=290)
    unidade_organica = models.CharField(max_length=260, blank=True, null=True, default=" ")
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return "%s" % (self.nome)

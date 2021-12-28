from django.db import models

# Create your models here.


class Curso(models.Model):
    nome = models.CharField(max_length=190)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")

    def __str__ (self):
        return "%s" % (self.nome)


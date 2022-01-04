"""
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-12-27 09:25:48
 * @modify date 2021-12-27 09:25:48
 * @desc [description]
 */
"""

from django.db import models
from curso.models import Curso
from config.models import Ano, Tremestre
# Create your models here.


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")
    codigo = models.CharField(max_length=20, blank=True, null=True, default="")
    carga_horaria = models.CharField(max_length=20, blank=True, null=True, default="")
    data_create= models.DateField(auto_now=True)

    def __str__(self):
        return "%s" % (self.nome)



class UnidadeCurricular_Curso(models.Model):
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, parent_link=True)
    tremestre = models.ForeignKey(Tremestre, on_delete=models.CASCADE, parent_link=True)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, parent_link=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, parent_link=True)
    ano_academico = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id

"""
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-12-27 09:25:48
 * @modify date 2021-12-27 09:25:48
 * @desc [description]
 */
"""

from django.db import models

# Create your models here.


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")
    codigo = models.CharField(max_length=20, blank=True, null=True, default="")
    carga_horaria = models.CharField(max_length=20, blank=True, null=True, default="")
    data_create= models.DateField(auto_now=True)

    def __str__(self):
        return "%s" % (self.nome)


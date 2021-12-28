"""
/**
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2021-12-27 08:45:47
 * @modify date 2021-12-27 08:45:47
 * @desc [description]
 */
"""

from django.contrib import admin
from arquivo.models import Arquivo, Tipologia
# Register your models here.


class ArquivoAdmin(admin.ModelAdmin):
    list_display =('autor', 'titulo','tipologia', 'partiilha','data')
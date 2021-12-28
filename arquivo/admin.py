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
from arquivo.models import Arquivo, Tipologia, Categoria_Partilha
# Register your models here.

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor', 'numero_pagina', 'tipologia', 'partilha', 'data')

admin.site.register(Tipologia)
admin.site.register(Categoria_Partilha)
admin.site.register(Arquivo, ArquivoAdmin)
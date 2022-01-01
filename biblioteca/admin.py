from django.contrib import admin

from biblioteca.models import Categoria_livro, Livro
# Register your models here.

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','categoria', 'numero_pagina', 'isbn', 'data_entrada')

admin.site.register(Categoria_livro)
admin.site.register(Livro, LivroAdmin)
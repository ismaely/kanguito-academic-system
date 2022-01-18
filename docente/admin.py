from django.contrib import admin
from docente.models import Docente, Docente_Grau_academico,Categoria, Estado_Docente
# Register your models here.

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('__str__','nome', 'numero_docente','categoria', 'grau_academico')
    
    @admin.display(ordering='pessoa_nome')
    def nome(self, obj):
        return obj.pessoa.nome
    
    def categoria_nome(self, obj):
        return obj.categoria.nome

    def grau_academico_nome(self, obj):
        return obj.grau_academico.nome

admin.site.register(Docente,DocenteAdmin)
admin.site.register(Docente_Grau_academico)
admin.site.register(Categoria)
admin.site.register(Estado_Docente)
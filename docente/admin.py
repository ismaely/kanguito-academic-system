from django.contrib import admin
from docente.models import Docente, Docente_Grau_academico,Categoria, Estado_Docente, Orientador, Estado_Orientador
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

class OrientadorAdmin(admin.ModelAdmin):
    list_display = ('__str__','docente', 'curso','estado')
    
    @admin.display(ordering='pessoa_nome')
    def docente(self, obj):
        return obj.docente.pessoa.nome
    
    def curso(self, obj):
        return obj.curso.nome

    def estado(self, obj):
        return obj.estado.nome


admin.site.register(Docente,DocenteAdmin)
admin.site.register(Docente_Grau_academico)
admin.site.register(Categoria)
admin.site.register(Estado_Docente)
admin.site.register(Estado_Orientador)
admin.site.register(Orientador, OrientadorAdmin)

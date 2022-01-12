from django.contrib import admin
from aluno.models import Aluno, Matricula

# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('__str__','pessoa_nome', 'numero_estudante','media_conclusao','instituicao_origem')
    empty_value_display = ''
    @admin.display(ordering='pessoa_nome')
    def pessoa_nome(self, obj):
        return obj.pessoa.nome

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('__str__','aluno_numero_estudante', 'curso_nome','opcao_matricula_nome', 'ano_nome','periodo_nome', 'dataMatricula')
    
    #@admin.display(ordering='pessoa_nome')
    def aluno_numero_estudante(self, obj):
        return obj.aluno_numero_estudante

    def curso_nome(self, obj):
        return obj.curso_nome

    def opcao_matricula_nome(self, obj):
        return obj.opcao_matricula_nome

    def ano_nome(self, obj):
        return obj.ano_nome

    def periodo_nome(self, obj):
        return obj.periodo_nome
                
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
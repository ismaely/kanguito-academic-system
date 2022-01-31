from django.contrib import admin
from aluno.models import Aluno, Matricula, Motivo_Reclamacao, Reclamacao, Motivo_Reclamacao

# Register your models here.


class ReclamacaoAdmin(admin.ModelAdmin):
    list_display = ('__str__','pessoa_nome', 'curso','motivo','descricao', 'data_reclamacao', 'estado')
    empty_value_display = ''
    #@admin.display(ordering='pessoa_nome')
    def pessoa_nome(self, obj):
        return obj.aluno.pessoa.nome
    
    def curso_nome(self, obj):
        return obj.curso.nome
    
    def motivo_nome(self, obj):
        return obj.motivo.nome


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('__str__','pessoa_nome', 'numero_estudante','media_conclusao','instituicao_origem')
    empty_value_display = ''
    @admin.display(ordering='pessoa_nome')
    def pessoa_nome(self, obj):
        return obj.pessoa.nome

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('__str__','numero_estudante', 'curso','opcao_matricula', 'ano','periodo', 'dataMatricula')
    
    #@admin.display(ordering='pessoa_nome')
    def numero_estudante(self, obj):
        return obj.aluno.numero_estudante

    def curso_nome(self, obj):
        return obj.curso.nome

    def opcao_matricula_nome(self, obj):
        return obj.opcao_matricula.nome

    def ano_nome(self, obj):
        return obj.ano.nome

    def periodo_nome(self, obj):
        return obj.periodo.nome


class Motivo_ReclamacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'opcao')
    empty_value_display = ''


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(Reclamacao, ReclamacaoAdmin)
admin.site.register(Motivo_Reclamacao, Motivo_ReclamacaoAdmin)
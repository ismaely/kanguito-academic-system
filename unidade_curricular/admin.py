from django.contrib import admin
from unidade_curricular.models import UnidadeCurricular, UnidadeCurricular_Curso
# Register your models here.

class Unidade_Admin(admin.ModelAdmin):
    list_display = ('id','nome','sigla', 'carga_horaria', 'codigo')

admin.site.register(UnidadeCurricular, Unidade_Admin)

class UnidadeCurricular_CursoAdmin(admin.ModelAdmin):
    list_display = ('unidade_curricular','curso', 'ano', 'tremestre', 'ano_academico')

admin.site.register(UnidadeCurricular_Curso, UnidadeCurricular_CursoAdmin)
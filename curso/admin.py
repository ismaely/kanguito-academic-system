from django.contrib import admin
from curso.models import Curso
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','unidade_organica','sigla')

admin.site.register(Curso, CursoAdmin)
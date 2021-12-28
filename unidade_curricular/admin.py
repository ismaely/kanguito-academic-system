from django.contrib import admin
from unidade_curricular.models import UnidadeCurricular
# Register your models here.

class Unidade_Admin(admin.ModelAdmin):
    list_display = ('id','nome','sigla', 'carga_horaria', 'codigo')

admin.site.register(UnidadeCurricular, Unidade_Admin)
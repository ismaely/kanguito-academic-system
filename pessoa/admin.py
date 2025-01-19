from django.contrib import admin

from pessoa.models import Pessoa, Dificiencia, Tipo_Dificiencia
# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome','genero','ndi','documento','data_nascimento','provincia','provincia','municipio')

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Dificiencia)
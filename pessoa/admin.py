from django.contrib import admin

from pessoa.models import Pessoa, Dificiencia, Tipo_Dificiencia
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Dificiencia)
from django.contrib import admin
from config.models import (Periodo, Provincia, Grau_academico, Municipio, Tremestre, Genero, Documento_identificacao,
 Estado_Civil, Pais, Ano, Opcao_Matricula, Contador_Numero )
# Register your models here.


admin.site.register(Provincia)
admin.site.register(Tremestre)
admin.site.register(Periodo)
admin.site.register(Grau_academico)
admin.site.register(Municipio)
admin.site.register(Genero)
admin.site.register(Estado_Civil)
admin.site.register(Documento_identificacao)
admin.site.register(Pais)
admin.site.register(Ano)
admin.site.register(Opcao_Matricula)
admin.site.register(Contador_Numero)
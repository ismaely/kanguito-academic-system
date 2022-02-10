from django.contrib import admin
from config.models import (Periodo, Provincia, Grau_academico, Municipio, Tremestre, Genero, Documento_identificacao,
 Estado_Civil, Pais, Ano, Opcao_Matricula, Contador_Numero )
# Register your models here.

class TremestreAdmin(admin.ModelAdmin):
    list_display = ('__str__','nome', 'ano')
  
    def ano_nome(self, obj):
        return obj.ano.nome

admin.site.register(Provincia)
admin.site.register(Tremestre, TremestreAdmin)
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

from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

app_name = 'aluno'
urlpatterns = [
    path('adicionarNovoCadastro_aluno/', views.adicionarNovoCadastro_aluno, name="adicionarNovoCadastro-aluno"),
    path('efectuar_reclamacao', views.efectuar_reclamacao, name="efectuar-reclamacao"),
    path('listar_reclamacao', views.listar_reclamacao, name="listar-reclamacao"),
    path('confirmacao_matricula', views.confirmacao_matricula, name="confirmacao-matricula"),
]

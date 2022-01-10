
from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

app_name = 'aluno'
urlpatterns = [
    path('adicionarNovoCadastro_aluno/', views.adicionarNovoCadastro_aluno, name="adicionarNovoCadastro-aluno"),
]

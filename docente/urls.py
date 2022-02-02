

from django.urls import path
from . import views

app_name = 'docente'

urlpatterns = [
  path('adicionar_docente/', views.adicionar_docente, name='adicionar-docente'),
  path('listar_docente/', views.listar_docente, name='listar-docente'),
  path('atualizar_dados_docente/<int:pk>/', views.atualizar_dados_docente, name='atualizar-dados-docente'),
  path('definirOrientador_teseTcc', views.definirOrientador_teseTcc, name='definirOrientador-tese'),
  path('listar_Orientador_teseTcc/', views.listar_Orientador_teseTcc, name='listar-Orientador-teseTcc'),
  path('atualizar_definirOrientador_teseTcc/<int:pk>/', views.atualizar_definirOrientador_teseTcc, name='atualizar-definirOrientador-teseTcc'),

]
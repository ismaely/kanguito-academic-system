

from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
  path('adicionarNovo_cursos/', views.adicionarNovo_cursos, name='adicionarNovo-cursos'),
  path('listar_cursos/', views.listar_cursos, name='listar-cursos'),
  path('atualizar_dadosCurso/<int:pk>/', views.atualizar_dadosCurso, name='atualizar-dadosCurso'),

 
]


from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
  path('AdicionarNovo_cursos/', views.AdicionarNovo_cursos, name='adicionarNovo-cursos'),
 
]
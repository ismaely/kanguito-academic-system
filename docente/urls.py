

from django.urls import path
from . import views

app_name = 'docente'

urlpatterns = [
  path('adicionar_docente/', views.adicionar_docente, name='adicionar-docente'),
  path('listar_docente/', views.listar_docente, name='listar-docente'),
  

]
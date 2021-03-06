
  
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'unidade_curricular'
urlpatterns = [
    path('adicionarNova_unidadeCurricular/', views.adicionarUnidadeCurricular, name= "nova-unidadeCurricular"),
    path('listarunidadeCurricular/', views.listarUnidadeCurricular, name= "listar-unidadeCurricular"),
    path('editarUnidadeCurricular/<int:pk>/', views.editarUnidadeCurricular, name= "editar-UnidadeCurricular"),
    path('definir_unidadeCurricular_curso/', views.definir_unidadeCurricular_curso, name= "definir-unidadeCurricular-curso"),
    path('listarUnidadeCurricular_cada_curso/', views.listarUnidadeCurricular_cada_curso, name= "listarUnidadeCurricular-cada-curso"),
]

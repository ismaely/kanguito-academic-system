from django.urls import path
from . import views

app_name = 'biblioteca'
urlpatterns = [

  path('adicionarNova_obraLiteraria/', views.adicionarNova_obraLiteraria, name='adicionarNova-obraLiteraria'),
  path('listar_obras/', views.listar_obras, name='listar-obras'),
  path('atualizar_obra_literaria/<int:pk>/', views.atualizar_obra_literaria, name='atualizar-obra-literaria'),
  path('consultar_obra/', views.consultaObra, name='consulta-obra'),

]
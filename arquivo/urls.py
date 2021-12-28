

from django.urls import path
from . import views

app_name = 'arquivo'

urlpatterns = [
  path('registar_arquivos/', views.registar_arquivos, name='registar-arquivos'),
  path('atualizar_arquivos/<int:pk>/', views.atualizar_arquivos, name='atualizar-arquivos'),
  path('listar_arquivos/', views.listar_arquivos, name='listar-arquivos'),
  path('atualizar_arquivos/<int:pk>/', views.atualizar_arquivos, name='atualizar-arquivos'),
  path('eliminar_arquivos/<int:pk>/', views.eliminar_arquivos, name='eliminar-arquivos'),
  path('visualizar_arquivo/<int:pk>/', views.visualizar_arquivo, name='visualizar-arquivo'),
]
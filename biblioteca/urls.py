from django.urls import path
from . import views

app_name = 'biblioteca'
urlpatterns = [
  path('adicionarNova_obraLiteraria/', views.adicionarNova_obraLiteraria, name='adicionarNova-obraLiteraria'),

]
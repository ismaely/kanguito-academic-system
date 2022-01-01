

from django.urls import path
from . import views

app_name = 'arquivo'

urlpatterns = [
  path('cadastrar_obra_literaria/', views.cadastrar_obra_literaria, name='cadastrar-obra'),

]
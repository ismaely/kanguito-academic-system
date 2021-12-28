

from django.urls import path
from . import views

app_name = 'arquivo'

urlpatterns = [
  path('registar_arquivos/', views.registar_arquivos, name='registar-arquivos'),

]
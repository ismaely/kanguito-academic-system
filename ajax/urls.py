
from django.urls import path
from . import views

app_name = 'ajax'
urlpatterns = [
    path('retorna_municipio/', views.retorna_municipio, name="retorna-municipio"),
]

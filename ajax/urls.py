
from django.urls import path
from . import views

app_name = 'ajax'
urlpatterns = [
    path('retorna_municipio/', views.retorna_municipio, name="retorna-municipio"),
    path('retorna_tremestre/', views.retorna_tremestre, name="retorna-tremestre"),
    path('retorna_as_unidadeCurricular/', views.retorna_as_unidadeCurricular, name="retorna-unidadeCurricular"),
]

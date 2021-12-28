
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'utilizador'
urlpatterns = [
    path('', views.loginUser, name='loginUser'),
    path('login/', views.loginUser, name='loginUser'),
    
]

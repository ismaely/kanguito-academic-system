"""kanguita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('utilizador.urls')),
    path('home/', include('home.urls')),
    path('aluno/', include('aluno.urls')),
    path('ajax/', include('ajax.urls')),
    path('unidade_curricular/', include('unidade_curricular.urls')),
    path('arquivo/', include('arquivo.urls')),
    path('biblioteca/', include('biblioteca.urls')),
    path('curso/', include('curso.urls')),
    path('docente/', include('docente.urls')),
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

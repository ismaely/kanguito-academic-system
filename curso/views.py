from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, FileResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import Q
from django.urls import reverse
import  sweetify, os
from django.conf import settings
from curso.forms import Curso_Form, Curso

# Create your views here.


#@login_required
def AdicionarNovo_cursos(request):
    form = Curso_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            curso = form.save()
            sweetify.success(request,'Curso Registado com sucesso!....', timer='4900', button='Ok')
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form': form}
    return render (request, 'secretaria/registar_cursos.html', context)
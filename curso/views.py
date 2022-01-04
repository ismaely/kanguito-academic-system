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
def listar_cursos(request):
    lista = Curso.objects.all().order_by('id')
    context = {'lista': lista}
    return render (request, 'curso/listar_curso.html', context)


def atualizar_dadosCurso(request, pk):
    resp = Curso.objects.get(id=pk)
    form = Curso_Form(request.POST or None, instance=resp)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            sweetify.success(request,'Dados atualizado com sucesso!....', timer='4900', button='Ok')
            return HttpResponseRedirect(reverse('curso:listar-cursos'))
    
    context = {'form': form, 'pk': resp.id}
    return render (request, 'curso/adicionar_novoCurso.html', context)


#@login_required
def adicionarNovo_cursos(request):
    form = Curso_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            curso = form.save()
            sweetify.success(request,'Curso Registado com sucesso!....', timer='4900', button='Ok')
            #return HttpResponseRedirect(reverse('secretaria:home'))
            form = Curso_Form()

    context = {'form': form}
    return render (request, 'curso/adicionar_novoCurso.html', context)

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import sweetify
from unidade_curricular.models import UnidadeCurricular, UnidadeCurricular_Curso
from unidade_curricular.forms import (UnidadeCurricularForm, UnidadeCurricular_Curso_Form, listarUnidadeCurricular_cada_curso_Form)
# Create your views here.



def listarUnidadeCurricular(request):
    lista =[]
    lista = UnidadeCurricular.objects.all()
    context = {'lista': lista}
    return render (request, 'unidadeCurricular/listarUnidadeCurricular.html', context)



#@login_required
def listarUnidadeCurricular_cada_curso(request):
    form = listarUnidadeCurricular_cada_curso_Form(request.POST or None)
    if request.method == "POST":
        curso = request.POST.get('curso')
        lista = UnidadeCurricular_Curso.objects.select_related('curso').filter(curso_id=curso).order_by('-id')
        context = {'lista':lista}
        return render (request, 'unidadeCurricular/lista_unidadeCada_curso.html', context)
    context = {'form':form}
    return render (request, 'unidadeCurricular/forms_listar_unidadeCurso.html', context)


# Editar dados da unidade curricular 
def editarUnidadeCurricular(request, pk):
    resp = UnidadeCurricular.objects.get(pk=pk)
    form = UnidadeCurricularForm(request.POST or None, instance=resp)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request,'Dados atualizado com sucesso',button='Ok', timer='3100', persistent="Close")
            return HttpResponseRedirect(reverse('unidade_curricular:listar-unidadeCurricular'))
    
    context = {'form':form, 'pk':pk}
    return render (request, 'unidadeCurricular/adicionarUnidadeCurricular.html', context)



def  definir_unidadeCurricular_curso(request):
    form =  UnidadeCurricular_Curso_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Inserida com sucesso!....', button='Ok', timer='3100', persistent="Close")
            form = UnidadeCurricular_Curso_Form()
           
    context = {'form':form}
    return render (request, 'unidadeCurricular/definir_unidadeCurricular_curso.html', context)



def adicionarUnidadeCurricular(request):
    form = UnidadeCurricularForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Unidade Curricular registrada com sucesso!....', button='Ok', timer='3100', persistent="Close")

            form = UnidadeCurricularForm()
            #return render (request, 'unidadeCurricular/adicionarUnidadeCurricular.html', context)

    context = {'form':form}
    return render (request, 'unidadeCurricular/adicionarUnidadeCurricular.html', context)


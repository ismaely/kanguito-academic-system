from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import sweetify
from unidade_curricular.forms import UnidadeCurricularForm, UnidadeCurricular
# Create your views here.


def adicionarUnidadeCurricular(request):
    form = UnidadeCurricularForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Unidade Curricular registrada com sucesso!....', button='Ok', timer='3100', persistent="Close")

            context = {'form': UnidadeCurricularForm()}
            return render (request, 'unidadeCurricular/adicionarUnidadeCurricular.html', context)

    context = {'form':form}
    return render (request, 'unidadeCurricular/adicionarUnidadeCurricular.html', context)



# Editar dados da unidade curricular 
def editarUnidadeCurricular(request, pk):
    resp = UnidadeCurricular.objects.get(pk=pk)
    form = UnidadeCurricularForm(request.POST or None, instance=resp)
    if request.method == 'POST':
        print("en.......")
        if form.is_valid():
            print("salvo..........")
            form.save()
            sweetify.success(request,'Dados atualizado com sucesso',button='Ok', timer='3100', persistent="Close")
            return HttpResponseRedirect(reverse('unidade_curricular:listar-unidadeCurricular'))
    
    context = {'form':form, 'pk':pk}
    return render (request, 'unidadeCurricular/adicionarUnidadeCurricular.html', context)



def listarUnidadeCurricular(request):
    lista =[]
    lista = UnidadeCurricular.objects.all()
    context = {'lista': lista}
    return render (request, 'unidadeCurricular/listarUnidadeCurricular.html', context)
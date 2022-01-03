from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, FileResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import Q
from django.urls import reverse
import  sweetify, os
from django.conf import settings
from biblioteca.models import Livro
from biblioteca.forms import Livro_Form,ConsultarForm


# Create your views here.

#@login_required
def listar_obras(request):
    lista = Livro.objects.select_related('categoria').all().order_by('-titulo')
    context = {'lista':lista}
    return render (request, 'biblioteca/listar_livros.html', context)



#@login_required
# função que vai efetuar a consulta dos dads quando for solicitado pela routa
def consultaObra(request):
    form = ConsultarForm(request.POST or None)
    if request.method == "POST":
        nome = request.POST['nome']
        lista = Livro.objects.filter(Q(titulo__contains=nome) | Q(autor__contains=nome))
        context = {'lista': lista}
        return render (request, 'biblioteca/listar_livros.html', context)

    context = {'form': form}
    return render (request, 'biblioteca/consultar_obras.html', context)



#@login_required
def atualizar_obra_literaria(request, pk):
    resp = Livro.objects.get(id=pk)
    form = Livro_Form(request.POST or None, instance=resp)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            sweetify.success(request,'Dados atualizado com sucesso!....', timer='4900', button='Ok')
            return HttpResponseRedirect(reverse('biblioteca:listar-obras'))
    #print(form.errors)
    context = {'form': form, 'pk': resp.id}
    return render (request, 'biblioteca/adicionarNova_obraLiteraria.html', context)


#@login_required
def adicionarNova_obraLiteraria(request):
    form = Livro_Form(request.POST or None)
    if request.method == "POST":
        form = Livro_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            sweetify.success(request,'Inserido com sucesso!..', timer='4900', button='Ok')
            #return HttpResponseRedirect(reverse('secretaria:home'))
            form = Livro_Form()
    
    context = {'form': form}
    return render (request, 'biblioteca/adicionarNova_obraLiteraria.html', context)


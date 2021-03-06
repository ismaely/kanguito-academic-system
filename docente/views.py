from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import sweetify
from django.db.models import Q
from docente.models import Docente, Orientador
from pessoa.models import Pessoa
from pessoa.forms import Pessoa_Form
from docente.forms import Docente_Form, ConsultarForm, OrientadorFrom
from config.views import prepara_foto

# Create your views here.


#@login_required
def listar_docente(request):
    lista = Docente.objects.select_related('pessoa').all().order_by('-pessoa')
    context = {'lista': lista}
    return render (request, 'docente/listar_docente.html', context)


def listar_Orientador_teseTcc(request):
    lista = Orientador.objects.select_related('docente').all().order_by('-docente')
    context = {'lista': lista}
    return render (request, 'docente/listar_Orientador.html', context)


def abriCandidatura_Orientador_teseTcc(request, pk):
    if pk > 0:
        orientador = Orientador.objects.get(id=pk)
        orientador.estado_id = 1
        orientador.save()
        sweetify.success(request,'Candidatura aberta com sucesso', button='Ok', timer='3100', persistent="Close")
        return HttpResponseRedirect(reverse('docente:listar-Orientador-teseTcc'))

    sweetify.error(request,'solicitação invalida', button='Ok', timer='3100', persistent="Close")
    return HttpResponseRedirect(reverse('docente:listar-Orientador-teseTcc'))


def fecharCandidatura_Orientador_teseTcc(request, pk):
    if pk > 0:
        orientador = Orientador.objects.get(id=pk)
        orientador.estado_id = 3
        orientador.save()
        sweetify.success(request,'Candidatura encerrada com sucesso', button='Ok', timer='3100', persistent="Close")
        return HttpResponseRedirect(reverse('docente:listar-Orientador-teseTcc'))

    sweetify.error(request,'solicitação invalida', button='Ok', timer='3100', persistent="Close")
    return HttpResponseRedirect(reverse('docente:listar-Orientador-teseTcc'))



def definirOrientador_teseTcc(request):
    form = OrientadorFrom(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request,'Orientador definido com sucesso', button='Ok', timer='3100', persistent="Close")
            form = OrientadorFrom()

    context = {'form': form}
    return render (request, 'docente/definirOrientador_teseTcc.html', context)



def atualizar_definirOrientador_teseTcc(request, pk):
    orientador = Orientador.objects.get(id=pk)
    form = OrientadorFrom(request.POST or None, instance=orientador)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sweetify.success(request,'Dados atualizado com sucesso', button='Ok', timer='3100', persistent="Close")
            return HttpResponseRedirect(reverse('docente:listar-Orientador-teseTcc'))

    context = {'form': form, 'pk': pk}
    return render (request, 'docente/definirOrientador_teseTcc.html', context)



#@login_required
def consultar_dados_docente(request):
    form = ConsultarForm(request.POST or None)
    if request.method == "POST":
        nome = request.POST['nome'].upper()
        lista = Docente.objects.filter(Q(pessoa_nome__contains=nome) | Q(autor__contains=nome))
        context = {'lista': lista}
        return render (request, 'arquivos/listar_arquivos.html', context)

    context = {'form': form}
    return render (request, 'docente/listar_docente.html', context)



def atualizar_dados_docente(request, pk):
    pessoa = Pessoa.objects.get(id=pk)
    resp = Docente.objects.get(pessoa_id=pk)
    form = Pessoa_Form(request.POST or None, instance=pessoa)
    form2 = Docente_Form(request.POST or None, instance=resp)
    if request.method == "POST":
        form = Pessoa_Form(request.POST, request.FILES or None, instance=pessoa)
        if form.is_valid() and form2.is_valid():

            pessoa = form.save(commit=False)
            pessoa.municipio_id = form.cleaned_data.get('municipio')
            if len(request.POST['foto']) > 0:
                pessoa.foto = prepara_foto(request)
                pessoa.save()
            else:
                pessoa.foto ='user.jpg'
                pessoa.save()
            form2.save()

            sweetify.success(request, 'Dados atualizado com sucesso!....', button='Ok', timer='3100', persistent="Close")
            form = Pessoa_Form()
            form2 = Pessoa_Form()
            
    context = {'form': form, 'form2': form2, 'pk': pk}
    return render(request,  'docente/adicionar_docente.html', context)



def adicionar_docente(request):
    form = Pessoa_Form(request.POST or None)
    form2 = Docente_Form(request.POST or None)
    if request.method == "POST":
        form = Pessoa_Form(request.POST, request.FILES or None)
        if form.is_valid() and form2.is_valid():

            pessoa = form.save(commit=False)
            pessoa.municipio_id = form.cleaned_data.get('municipio')
            if len(request.POST['foto']) > 0:
                pessoa.foto = prepara_foto(request)
                pessoa.save()
            else:
                pessoa.foto ='user.jpg'
                pessoa.save()
            docente = form2.save(commit=False)
            docente.pessoa_id = pessoa.id
            docente.save()

            sweetify.success(request, 'Dados registado com sucesso!....', button='Ok', timer='3100', persistent="Close")
            form = Pessoa_Form()
            form2 = Pessoa_Form()
            
    context = {'form': form, 'form2': form2}
    return render(request,  'docente/adicionar_docente.html', context)


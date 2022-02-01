from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import sweetify
from environment.env import DATA_HORA_ZONA, DATA_ANO
from aluno.forms import Aluno_Form, Matricula_Form, Reclamacao_Form
from pessoa.forms import Pessoa_Form
from config.views import prepara_foto
from aluno.models import Reclamacao
# Create your views here.



def listar_reclamacao(request):
    lista =  Reclamacao.objects.select_related('aluno').all()
    context = {'lista': lista}
    
    return render(request, 'aluno/listar_reclamacao.html', context)



def efectuar_reclamacao(request):
    form = Reclamacao_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            recl = form.save(commit=False)
            recl.aluno_id = form.cleaned_data['aluno']
            recl.save()
            sweetify.success(request, 'Reclamação feita com sucesso!...', button='Ok', timer='3100', persistent="Close")
            form = Reclamacao_Form()

    context = {'form': form}
    return render(request, 'aluno/efecturReclamacao.html', context)



def adicionarNovoCadastro_aluno(request):
    form = Pessoa_Form(request.POST or None)
    form2 = Aluno_Form(request.POST or None)
    form3 = Matricula_Form(request.POST or None)
    if request.method == 'POST':
        form = Pessoa_Form(request.POST, request.FILES or None)
        if form.is_valid() and form2.is_valid():
            curso = request.POST.get('curso')
           
            pessoa = form.save(commit=False)
            pessoa.municipio_id = form.cleaned_data.get('municipio')
            if len(request.POST['foto']) > 0:
                pessoa.foto = prepara_foto(request)
                pessoa.save()
            else:
                pessoa.foto ='user.jpg'
                pessoa.save()
            dados = form2.save(commit=False)
            dados.pessoa_id = pessoa.id
            dados.curso_id = curso
            dados.save()
            resp = form3.save(commit=False)
            resp.aluno_id = dados.id
            resp.save()

            sweetify.success(request, 'Dados registado com sucesso!....', button='Ok', timer='3100', persistent="Close")

            context = {'pessoa': form.instance, 'aluno': form2.instance, 'matricula': form3.instance}
            return render (request, 'aluno/reciboInscricao.html', context)

    context = {'form':form,'form2': form2,'form3':form3}
    return render (request, 'aluno/adicionarNovoCadastro-aluno.html', context)
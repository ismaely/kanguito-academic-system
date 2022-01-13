from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import json, sweetify, random, base64
from environment.env import DATA_HORA_ZONA 
from aluno.forms import Aluno_Form, Matricula_Form
from pessoa.forms import Pessoa_Form
# Create your views here.



"""
função que vai prepara a foto que vai ser salva
"""
def prepara_foto(request):
    img = request.POST["foto"]
    nome = str(DATA_HORA_ZONA).split('.')
    foto = []
    inicio = img.find(',')
    imagem = img[inicio+1:]

    with open("./media/fotos/"+ str(nome[0]) + "_" + str(random.random()) + ".png", "wb") as fh:
        fh.write(base64.b64decode(imagem))
        foto = str(fh).split('=')
        um = foto[1].replace(">", '')

    um = um.replace("'", '')
    um = um.split('media/')
    return um[1]



def adicionarNovoCadastro_aluno(request):
    form = Pessoa_Form(request.POST or None)
    form2 = Aluno_Form(request.POST or None)
    form3 = Matricula_Form(request.POST or None)
    if request.method == 'POST':
        form = Pessoa_Form(request.POST, request.FILES or None)
        if form.is_valid() and form2.is_valid():
            curso = request.POST.get('curso')
            print("------------------------")
            print(curso)
            print("------------------------")
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

    context = {'form':form,'form2':form2,'form3':form3}
    return render (request, 'aluno/adicionarNovoCadastro-aluno.html', context)
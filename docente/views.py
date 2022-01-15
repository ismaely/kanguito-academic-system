from django.shortcuts import render
import sweetify
from docente.models import Docente
from pessoa.forms import Pessoa_Form
from docente.forms import Docente_Form
from config.views import prepara_foto

# Create your views here.


def adicionar_docente(request):
    form = Pessoa_Form(request.POST or None)
    form2 = Docente_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid() and form2.is_valid():

            pessoa = form.save(commit=False)
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


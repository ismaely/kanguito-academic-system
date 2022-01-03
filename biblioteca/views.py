from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, FileResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import Q
from django.urls import reverse
import  sweetify, os
from django.conf import settings
from biblioteca.models import Livro
from biblioteca.forms import Livro_Form


# Create your views here.


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
    #print(form.errors)
    context = {'form': form}
    return render (request, 'biblioteca/adicionarNova_obraLiteraria.html', context)


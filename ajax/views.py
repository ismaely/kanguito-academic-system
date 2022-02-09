from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, Http404, HttpResponse
import random, json
from config.models import Municipio
from unidade_curricular.models import UnidadeCurricular_Curso
from config.models import Ano, Tremestre

# Create your views here.


def retorna_municipio(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = [(k.id, k.nome)for k in Municipio.objects.filter(provincia_id=int(id))]
            dados = {
                'muncipios':  lista,
            }
        return JsonResponse(dados)
    except ValueError:
        print(" ERRO RETORNO DOS MUNICIPIOS")


# Função que vai retotna os tremestre, qdo selecionar o ano.
def retorna_tremestre(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            id = valor['id']
            lista = [(k.id, k.nome)for k in Tremestre.objects.filter(ano_id=int(id))]
            dados = {
                'resposta':  lista,
            }
        return JsonResponse(dados)
    except ValueError:
        print(" ERRO RETORNO OS TREMESTRE")

from django.shortcuts import render
from config.models import Contador_Numero
from environment.env import DATA_ANO


# Create your views here.


def gerarNumeroEstudante():
    try:

        contador = int(resp.numero) + 1
        resp.numero =  contador
        novo_numero = str(contador)
        resp.save()

        atribuindo = DATA_ANO
        atribuindo += novo_numero
        return atribuindo
    except Exception as e:
        print('falha no ao atrbuir o numeroo de estaudante')
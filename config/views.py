from django.shortcuts import render
from config.models import Contador_Numero
from environment.env import DATA_ANO, DATA_HORA_ZONA
import random, base64



# FUNÇÃO QUE VAI PREPARAR A FOTO Q SERA SALVA,  E QUE VVAI GUARDAR NA PASTA DE FOTOS
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



# FUNÇÃO QUE VAI GERAR O NUMERO DO ALUNO
def gerarNumeroEstudante():
    try:
        resp = Contador_Numero.objects.first()
        contador = int(resp.numero) + 1
        resp.numero =  contador
        novo_numero = str(contador)
        resp.save()

        atribuindo = DATA_ANO
        atribuindo += novo_numero
        return atribuindo
    except Exception as e:
        print('falha no ao atrbuir o numeroo de estaudante')
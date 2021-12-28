from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def loginUser(request):
    context = {}
    return render (request, 'utilizador/login.html', context)


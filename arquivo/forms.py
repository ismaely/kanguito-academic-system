from django import forms
from django.forms import ModelForm
from arquivo.models import Arquivo


class Arquivo_Form(ModelForm):
    class Meta:
        arquivo = forms.CharField(widget=forms.TextInput(attrs={'type': 'file','class': 'file-upload-default'}))
        model = Arquivo
        fields = ['titulo', 'autor', 'numero_pagina', 'tipologia', 'data', 'partilha', 'arquivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_pagina': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'tipologia': forms.Select(attrs={'class': 'form-control'}),
            'partilha': forms.Select(attrs={'class': 'form-control'}),
        }


class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

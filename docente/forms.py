from django import forms
from django.forms import ModelForm
from docente.models import Docente, Orientador
from config.views import gerarNumeroEstudante



class Docente_Form(ModelForm):
    class Meta:
        pessoa = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        model = Docente
        fields = ['numero_docente', 'categoria','grau_academico', 'data_registro', 'estado']
        widgets = {
            'numero_docente': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select( attrs={'class': 'form-control '}),
            'estado': forms.Select( attrs={'class': 'form-control '}),
            'grau_academico': forms.Select( attrs={'class': 'form-control '}),
            'data_registro': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
        }


class OrientadorFrom(ModelForm):
    class Meta:
        model = Orientador
        fields = ['docente','curso', 'data_limite', 'estado']
        widgets = {
            'docente': forms.Select( attrs={'class': 'form-control '}),
            'estado': forms.Select( attrs={'class': 'form-control '}),
            'curso': forms.Select( attrs={'class': 'form-control '}),
            'data_limite': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
        }


class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

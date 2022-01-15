from django import forms
from django.forms import ModelForm
from docente.models import Docente
from config.views import gerarNumeroEstudante



class Docente_Form(ModelForm):
    class Meta:
        pessoa = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        model = Docente
        fields = ['numero_docente', 'categoria','grau_academico']
        widgets = {
            'numero_docente': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select( attrs={'class': 'form-control '}),
            'grau_academico': forms.Select( attrs={'class': 'form-control '}),
        }


class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

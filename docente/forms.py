from django import forms
from django.forms import ModelForm
from docente.models import Docente, Orientador, Unidade_Curricular_Docente
from config.views import gerarNumeroEstudante



class Docente_Form(ModelForm):
    pessoa = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
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
        fields = ['docente','curso', 'data_limite', 'estado','numero_orientados']
        widgets = {
            'docente': forms.Select( attrs={'class': 'form-control '}),
            'estado': forms.Select( attrs={'class': 'form-control '}),
            'curso': forms.Select( attrs={'class': 'form-control '}),
            'data_limite': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'numero_orientados': forms.NumberInput(attrs={'type': 'integer','class': 'form-control'}),
        }


class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class atribuirUnidade_docenteForm(ModelForm):
    #ano_letivo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Unidade_Curricular_Docente
        fields = ['docente','curso', 'unidadeCurricular','periodo', 'nivel_academico','ano_letivo', 'tremestre','data_registro']
        widgets = {
            'docente': forms.Select( attrs={'class': 'form-control '}),
            'estado': forms.Select( attrs={'class': 'form-control '}),
            'curso': forms.Select( attrs={'class': 'form-control '}),
            'unidadeCurricular': forms.Select( attrs={'class': 'form-control '}),
            'periodo': forms.Select( attrs={'class': 'form-control '}),
            'ano_letivo': forms.TextInput(attrs={'class': 'form-control'}),
            'tremestre': forms.Select( attrs={'class': 'form-control '}),
            'nivel_academico': forms.Select( attrs={'class': 'form-control '}),
            'data_registro': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
        }

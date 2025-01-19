from django import forms
from django.forms import ModelForm
from curso.models import Curso



class Curso_Form(ModelForm):
    class Meta:
        model = Curso
        fields = ['nome','unidade_organica', 'sigla']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'unidade_organica': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
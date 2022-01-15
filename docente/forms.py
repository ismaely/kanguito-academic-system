from django import forms
from django.forms import ModelForm
from aluno.models import Aluno, Pessoa, Matricula
from config.views import gerarNumeroEstudante



"""class Aluno_Form(ModelForm):
    class Meta:
        curso = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        #numero_estudante = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        model = Aluno
        fields = ['media_conclusao', 'instituicao_origem', 'numero_estudante', 'grau_academico','area_formacao', 'curso_frequentado']
        widgets = {
            'curso_frequentado': forms.TextInput(attrs={'class': 'form-control'}),
            'area_formacao': forms.TextInput(attrs={'class': 'form-control'}),
            'media_conclusao': forms.TextInput(attrs={'class': 'form-control'}),
            'instituicao_origem': forms.TextInput(attrs={'class': 'form-control'}),
            'grau_academico': forms.Select( attrs={'class': 'form-control '}),
            'numero_estudante': forms.TextInput(attrs={'class': 'form-control'}),
        }
 """   

class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

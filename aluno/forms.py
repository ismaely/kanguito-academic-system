from django import forms
from django.forms import ModelForm
from aluno.models import Aluno, Pessoa, Matricula



class Aluno_Form(ModelForm):
    class Meta:
        curso = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        model = Aluno
        fields = ['media_conclusao', 'instituicao_origem', 'numero_estudante', 'grau_academico','area_formacao', 'curso_frequentado']
        widgets = {
            'curso_frequentado': forms.TextInput(attrs={'class': 'form-control'}),
            'area_formacao': forms.TextInput(attrs={'class': 'form-control'}),
            'media_conclusao': forms.TextInput(attrs={'class': 'form-control'}),
            'instituicao_origem': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_estudante': forms.TextInput(attrs={'class': 'form-control'}),
            'grau_academico': forms.Select( attrs={'class': 'form-control '}),
        }


class Matricula_Form(ModelForm):
    class Meta: 
        aluno = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        model = Matricula
        fields = ['curso', 'opcao_matricula', 'ano', 'tremestre','periodo','nota_exame','dataMatricula']
        widgets = {
            'curso': forms.Select( attrs={'class': 'form-control '}),
            'opcao_matricula': forms.Select( attrs={'class': 'form-control '}),
            'ano': forms.Select( attrs={'class': 'form-control '}),
            'periodo': forms.Select( attrs={'class': 'form-control '}),
            'tremestre': forms.Select(attrs={'class': 'form-control'}),
            'nota_exame': forms.TextInput(attrs={'class': 'form-control'}),
            'dataMatricula': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
        }



class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

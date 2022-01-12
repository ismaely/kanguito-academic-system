from django import forms
from django.forms import ModelForm
from aluno.models import Aluno, Pessoa



class Aluno_Form(ModelForm):
    class Meta:
        #nome = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        model = Aluno
        fields = ['media_conclusao', 'instituicao_origem', 'data_registro', 'numero_estudante']
        widgets = {
            'media_conclusao': forms.TextInput(attrs={'class': 'form-control'}),
            'instituicao_origem': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_estudante': forms.TextInput(attrs={'class': 'form-control'}),
            'data_registro': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

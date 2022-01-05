from django import forms
from django.forms import ModelForm
from unidade_curricular.models import UnidadeCurricular, UnidadeCurricular_Curso



class UnidadeCurricularForm(ModelForm):
    class Meta:
        model = UnidadeCurricular
        fields = ['nome', 'codigo', 'sigla', 'carga_horaria']
        widgets = {
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'carga_horaria': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        

class UnidadeCurricular_Curso_Form(ModelForm):
    class Meta:
        model =  UnidadeCurricular_Curso
        fields = ('curso', 'unidade_curricular', 'ano', 'tremestre', 'ano_academico')
        widgets = {
            'ano_academico': forms.TextInput(attrs={'class': 'form-control'}),
            'unidade_curricular': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control'}),
            'tremestre': forms.Select(attrs={'class': 'form-control'}),
        }


class listarUnidadeCurricular_cada_curso_Form(ModelForm):
    class Meta:
        model = UnidadeCurricular_Curso
        fields = ('curso',)
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }

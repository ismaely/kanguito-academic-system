from django import forms
from django.forms import ModelForm
from unidade_curricular.models import UnidadeCurricular



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
        
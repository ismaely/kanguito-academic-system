"""**
 * @author [Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2022-02-09 16:48:31
 * @modify date 2022-02-09 16:48:31

 """

from django import forms
from django.forms import ModelForm
from aluno.models import Aluno, Matricula, Reclamacao, Confirmar_Matricula
from config.views import gerarNumeroEstudante, retornaId



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
            'grau_academico': forms.Select(attrs={'class': 'form-control '}),
            'numero_estudante': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_numero_estudante(self):
        numero_estudante = self.cleaned_data.get('numero_estudante')
        if numero_estudante is None or numero_estudante == "":
            numero_estudante = gerarNumeroEstudante()
        return numero_estudante


class Matricula_Form(ModelForm):
    aluno = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta: 
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


class Reclamacao_Form(ModelForm):
    aluno = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Reclamacao
        fields = ['curso', 'motivo', 'data_reclamacao', 'descricao']
        widgets = {
            #'aluno': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'curso': forms.Select( attrs={'class': 'form-control '}),
            'motivo': forms.Select( attrs={'class': 'form-control '}),
            'data_reclamacao': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            
        }

    def clean_aluno(self):
        aluno = self.cleaned_data.get('aluno')
        resp = retornaId(aluno)
        aluno = resp
        if int(resp) == 0:
            raise forms.ValidationError("o numero de indetificação não é valido")
        return resp


class Confirmar_Matricula_Form(ModelForm):
    aluno = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tremestre = forms.CharField(max_length=60,required=False,  widget=forms.Select(choices="", attrs={'class': 'form-control ajax_tremestre'}))
    cadeiras_atraso = forms.CharField(max_length=60,required=False,  widget=forms.Select(choices="", attrs={'class': 'form-control ajax_cadeiras_atraso'}))
    class Meta:
        model = Confirmar_Matricula
        fields = ['curso', 'periodo', 'ano', 'data_confirmacao', 'numero_recibo']
        widgets = {
            'curso': forms.Select( attrs={'class': 'form-control ajax_curso'}),
            'periodo': forms.Select( attrs={'class': 'form-control'}),
            'ano': forms.Select( attrs={'class': 'form-control ajax_ano'}),
            'data_confirmacao': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            #'cadeiras_atraso': forms.Select(attrs={'class': 'form-control '}),
            'numero_recibo': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            #'tremestre': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_aluno(self):
        aluno = self.cleaned_data.get('aluno')
        resp = retornaId(aluno)
        aluno = resp
        if int(resp) == 0:
            raise forms.ValidationError("o numero de indetificação não é valido")
        return resp
    


class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

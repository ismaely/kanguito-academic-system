from django import forms
from django.forms import ModelForm
from aluno.models import Aluno, Matricula, Reclamacao
from config.views import gerarNumeroEstudante, retornaId



class Aluno_Form(ModelForm):
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
            'grau_academico': forms.Select(attrs={'class': 'form-control '}),
            'numero_estudante': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_numero_estudante(self):
        numero_estudante = self.cleaned_data.get('numero_estudante')
        
        if numero_estudante is None or numero_estudante == "":
            numero_estudante = gerarNumeroEstudante()
        
        return numero_estudante


class Matricula_Form(ModelForm):
    class Meta: 
        aluno = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        #numero_estudante = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
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
    class Meta:
        aluno = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
        model = Reclamacao
        fields = [ 'curso', 'motivo', 'data_reclamacao','descricao']
        widgets = {
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
            return aluno


class ConsultarForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

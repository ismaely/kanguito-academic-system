"""/
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2022-01-10 09:58:27
 * @modify date 2022-01-10 09:58:27
 * @desc [description]
 */
 """
from django import forms
from django.forms import ModelForm
from pessoa.models import Pessoa
from environment.env import DATA_ANO

class Pessoa_Form(ModelForm):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}))
    nome_pai = forms.CharField(max_length=100, required=False,  widget=forms.TextInput(attrs={'class': 'form-control '}))
    nome_mae = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={ 'class': 'form-control '}))
    ndi = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
    residencia = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=180, required=False, widget=forms.TextInput(attrs={'class': 'form-control', }))
    municipio = forms.CharField(max_length=60,required=False,  widget=forms.Select(choices="", attrs={'class': 'form-control ajax_municipio'}))
    foto = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'fotoSalva'}))
    data_nascimento = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'type':'date', 'class': 'form-control '}))
    class Meta:
        model = Pessoa
        fields = ['nome', 'nome_pai', 'nome_mae','genero','data_nascimento', 'estado_civil', 'residencia', 'provincia', 'telefone',
        'documento', 'email', 'nacionalidade','ndi', 'foto']

        widgets = {
            'provincia': forms.Select(attrs={'class': 'form-control ajax_provincia'}),
            'genero': forms.Select( attrs={'class': 'form-control'}),
            'estado_civil': forms.Select( attrs={'class': 'form-control'}),
            'documento': forms.Select( attrs={'class': 'form-control'}),
            'nacionalidade': forms.Select( attrs={'class': 'form-control'}),
        }

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        data = []
        data = data_nascimento.split('-')
        idade = int(DATA_ANO) - int(data[0])
        if idade < 17:
            raise forms.ValidationError("É menor de idade...")
        
        return data_nascimento
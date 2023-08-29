# questionarioapp/forms.py

from django import forms

class QuestionarioForm(forms.Form):
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Título do Questionário'}))
    explicacao = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Explicação do Questionário'}))
    questoes_alternativas = forms.CharField(widget=forms.HiddenInput)
    

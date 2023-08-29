# questionarioapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionario, Questao, Alternativa
from .forms import QuestionarioForm
import json

def edit(request):
    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            explicacao = form.cleaned_data['explicacao']
            questionario = Questionario.objects.create(titulo=titulo, explicacao=explicacao)
            
            # Obter os dados das questões e alternativas do campo oculto
            questoes_alternativas_json = form.cleaned_data['questoes_alternativas']
            questoes_alternativas = json.loads(questoes_alternativas_json)
            
            for q_a in questoes_alternativas:
                questao_titulo = q_a['questao']
                alternativas = q_a['alternativas']
                questao = Questao.objects.create(questionario=questionario, titulo=questao_titulo)
                for alternativa_texto in alternativas:
                    Alternativa.objects.create(questao=questao, texto=alternativa_texto)
            
            return redirect('lista_questionarios')  # Redireciona para a página de listagem
    else:
        form = QuestionarioForm()
    
    return render(request, "edit.html", {"form": form})


def lista_questionarios(request):
    questionarios = Questionario.objects.all()
    return render(request, 'lista_questionarios.html', {'questionarios': questionarios})


def detalhes_questionario(request, questionario_id):
    questionario = Questionario.objects.get(pk=questionario_id)
    return render(request, 'detalhes_questionario.html', {'questionario': questionario})


def excluir_questionario(request, questionario_id):
    questionario = get_object_or_404(Questionario, pk=questionario_id)
    
    if request.method == 'POST':
        questionario.delete()
        return redirect('lista_questionarios')
    
    return render(request, 'excluir_questionario.html', {'questionario': questionario})
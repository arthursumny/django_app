# questionarioapp/views.py

from django.http import JsonResponse
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
            
            questoes_alternativas_json = form.cleaned_data['questoes_alternativas']
            questoes_alternativas = json.loads(questoes_alternativas_json)
            
            for q_a in questoes_alternativas:
                questao_titulo = q_a['questao']
                alternativas = q_a['alternativas']
                questao = Questao.objects.create(questionario=questionario, titulo=questao_titulo)
                for alternativa_texto in alternativas:
                    alternativa_parts = alternativa_texto.split("{")
                    alternativa_text = alternativa_parts[0].strip()
                    pontuacao_part = alternativa_parts[1].split("}")
                    pontuacao = int(pontuacao_part[0].strip()) if len(pontuacao_part) > 1 else 0
                    Alternativa.objects.create(questao=questao, texto=alternativa_text, pontuacao=pontuacao)
            
            return redirect('lista_questionarios')
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

def editar_questionario(request, questionario_id):
    questionario = Questionario.objects.get(pk=questionario_id)
    return render(request, 'editar_questionario.html', {'questionario': questionario})

def save_edits(request, questionario_id):
    if request.method == 'POST':
        questionario = Questionario.objects.get(id=questionario_id)
        questionario.titulo = request.POST.get('titulo')
        questionario.explicacao = request.POST.get('explicacao')
        questionario.save()

        # Atualize as questões e alternativas
        questoes_alternativas = json.loads(request.POST.get('questoes_alternativas'))

        for q_a in questoes_alternativas:
            questao_titulo = q_a['questao']
            alternativas = q_a['alternativas']

            try:
                questao = questionario.questao_set.get(titulo=questao_titulo)
                questao.alternativa_set.all().delete()  # Remove as alternativas antigas

                for alternativa_texto in alternativas:
                    alternativa_parts = alternativa_texto.split("{")
                    alternativa_text = alternativa_parts[0].strip()
                    pontuacao_part = alternativa_parts[1].split("}")
                    pontuacao = int(pontuacao_part[0].strip()) if len(pontuacao_part) > 1 else 0
                    Alternativa.objects.create(questao=questao, texto=alternativa_text, pontuacao=pontuacao)
            except Questao.DoesNotExist:
                pass  # Questão não existe, não precisa atualizar

        return JsonResponse({"message": "Edições salvas com sucesso!"})

        # Redirecionar para a página de detalhes do questionário
        #return redirect('detalhes_questionario', questionario_id=questionario.id)

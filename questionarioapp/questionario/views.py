# questionarioapp/views.py

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionario, Questao, Alternativa, Score
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
                    alternativa = Alternativa.objects.create(questao=questao, texto=alternativa_text, pontuacao=pontuacao)
                    
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
                    alternativa = Alternativa.objects.create(questao=questao, texto=alternativa_text, pontuacao=pontuacao)
                    
            score_intervals_json = form.cleaned_data['score_intervals']
            score_intervals = json.loads(score_intervals_json)
                    
            for s_i in score_intervals:
                explicacao_parts = s_i.split("{")
                explicacao_text = explicacao_parts[0].strip()
                pontuacao_part = explicacao_parts[1].split("}")
                pontuacao = int(pontuacao_part[0].strip()) if len(pontuacao_part) > 1 else 0
                score = Score.objects.create(questionario=questionario, explicacao=explicacao_text, pontuacao=pontuacao)
            return redirect('lista_questionarios')
    else:
        form = QuestionarioForm()

    return render(request, "edit.html", {"form": form})


def edit_questionario(request, questionario_id):
    questionario = get_object_or_404(Questionario, pk=questionario_id)

    titulo = questionario.titulo
    explicacao = questionario.explicacao

    questoes = questionario.questao_set.all()

    alternativas = []
    for questao in questoes:
        alternativas.append(questao.alternativa_set.all())

    if request.method == 'POST':
        questionario.titulo = request.POST.get('titulo')
        questionario.explicacao = request.POST.get('explicacao')
        questionario.save()

        for i, questao in enumerate(questoes):
            questao.titulo = request.POST.get(f'questao-titulo-{i}')
            questao.save()

            for j, alternativa in enumerate(alternativas[i]):
                alternativa.texto = request.POST.get(f'alternativa-{i}-{j}')
                alternativa.pontuacao = request.POST.get(f'pontuacao-{i}-{j}')
                alternativa.save()

        return redirect('detalhes_questionario', questionario_id)

    return render(request, 'edit_questionario.html', {
        'questionario': questionario,
        'titulo': titulo,
        'explicacao': explicacao,
        'questoes': questoes,
        'alternativas': alternativas,
    })
    
def edit_score(request):
    scores = Score.objects.all()

    if request.method == 'POST':
        # Process and save the score and explanation data
        scores = request.POST.getlist('score')
        explanations = request.POST.getlist('explanation')
        score_intervals = request.POST.getlist('score_intervals', ['0'])  # Assign default value of '0'

        for i in range(len(scores)):
            score = scores[i]
            explanation = explanations[i]
            interval = score_intervals[i]
            score_obj = Score.objects.get(id=score)
            score_obj.pontuacao = score if score else '0'
            score_obj.explicacao = explanation if explanation else ''
            score_obj.save()

        return redirect('edit_questionario')

    return render(request, 'edit_intervals.html', {'scores': scores})

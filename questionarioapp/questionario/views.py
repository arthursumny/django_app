# questionarioapp/views.py

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionario, Questao, Alternativa, Questao1, Alternativa1
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
                    
            questoes_alternativas_json1 = form.cleaned_data['questoes_alternativas1']
            questoes_alternativas1 = json.loads(questoes_alternativas_json1)
            
            for q_a1 in questoes_alternativas1:
                questao_titulo1 = q_a1['questao1']
                alternativas1 = q_a1['alternativas1']
                questao1 = Questao1.objects.create(questionario=questionario, titulo1=questao_titulo1)
                alternativa_part1 = alternativas1.split("#")
                alternativa_text1 = alternativa_part1[0].strip()
                pontuacao1 = int(alternativa_part1[1].strip())
                alternativa1 = Alternativa1.objects.create(questao1=questao1, texto1=alternativa_text1, pontuacao1=pontuacao1)
                           
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
    
def edit_nivel(request, questionario_id):
    questionario = get_object_or_404(Questionario, pk=questionario_id)
    
    titulo = questionario.titulo
    explicacao = questionario.explicacao
    
    questoes1 = questionario.questao1_set.all()
    
    alternativas1 = []
    for questao1 in questoes1:
        alternativas1.append(questao1.alternativa1_set.all())
        
    if request.method == 'POST':
        questionario.titulo = request.POST.get('titulo')
        questionario.explicacao = request.POST.get('explicacao')
        questionario.save()
        
        for i, questao1 in enumerate(questoes1):
            questao1.titulo1 = request.POST.get(f'questao1-titulo-{i}')
            questao1.save()
            
            for j, alternativa1 in enumerate(alternativas1[i]):
                alternativa1.texto1 = request.POST.get(f'alternativa1-{i}-{j}')
                alternativa1.pontuacao1 = request.POST.get(f'pontuacao1-{i}-{j}')
                alternativa1.save()
        
        return redirect('detalhes_questionario', questionario_id)
    
    return render(request, 'edit_nivel.html', {
        'questionario': questionario,
        'titulo': titulo,
        'explicacao': explicacao,
        'questoes': questoes1,
        'alternativas1': alternativas1,
        
    })
        
  

   

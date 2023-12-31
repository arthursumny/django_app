# questionarioapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionario, Questao, Alternativa, Nivel, Explicacao
from .forms import QuestionarioForm
from django.conf import settings
import json
from django.core.mail import send_mail

def edit(request):
    if request.method == 'POST':
        form = QuestionarioForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            explicacao = form.cleaned_data['explicacao']
            questionario = Questionario.objects.create(titulo=titulo, explicacao=explicacao)
            imagem = request.FILES.get('image')
            
            questionario.imagem = form.cleaned_data['imagem']
            questionario.save()

            questoes_alternativas_json = form.cleaned_data['questoes_alternativas']
            questoes_alternativas = json.loads(questoes_alternativas_json)

            for q_a in questoes_alternativas:
                questao_titulo = q_a['questao']
                alternativas = q_a['alternativas']
                questao = Questao.objects.create(questionario=questionario, titulo=questao_titulo)
                for alternativa_texto in alternativas:
                    alternativa_parts = alternativa_texto.split("#")
                    if len(alternativa_parts) == 2:
                        texto_alternativa = alternativa_parts[0].strip()
                        pontuacao = int(alternativa_parts[1].strip())
                        alternativa = Alternativa.objects.create(questao=questao, texto=texto_alternativa, pontuacao=pontuacao)
                    
            questoes_alternativas_json1 = form.cleaned_data['questoes_alternativas1']
            questoes_alternativas1 = json.loads(questoes_alternativas_json1)
            
            for q_a1 in questoes_alternativas1:
                questao_titulo1 = q_a1['questao1']
                alternativas1 = q_a1['alternativas1']
                questao1 = Nivel.objects.create(questionario=questionario, titulo=questao_titulo1)
                alternativa_part1 = alternativas1.split("#")
                alternativa_text1 = alternativa_part1[0].strip()
                pontuacao1 = int(alternativa_part1[1].strip())
                alternativa1 = Explicacao.objects.create(nivel=questao1, texto=alternativa_text1, pontuacao=pontuacao1)
                           
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
    image = questionario.imagem

    questoes = questionario.questao_set.all()
    niveis = questionario.nivel_set.all()

    alternativas = []
    for questao in questoes:
        alternativas.append(questao.alternativa_set.all())

    if request.method == 'POST':
        nova_imagem = request.FILES.get('nova_imagem')
        imagem_atual = request.POST.get('imagem_atual')
        questionario.titulo = request.POST.get('titulo')
        questionario.explicacao = request.POST.get('explicacao')
        questionario.imagem = request.FILES.get('image')
        
        if nova_imagem:
            questionario.imagem = nova_imagem
        elif imagem_atual:
            questionario.imagem = imagem_atual
            
        questionario.save()


        
        for i, questao in enumerate(questoes):
            questao.titulo = request.POST.get(f'questao-titulo-{i}')
            questao.save()
            

            for j, alternativa in enumerate(alternativas[i]):
                alternativa.texto = request.POST.get(f'alternativa-{i}-{j}')
                alternativa.pontuacao = request.POST.get(f'pontuacao-{i}-{j}')
                alternativa.save()
                

        for i, nivel in enumerate(niveis):
            nivel.titulo = request.POST.get(f'nivel-titulo-{i}')
            nivel.save()
            
            
            for j, explicacao in enumerate(nivel.explicacao_set.all()):
                explicacao.texto = request.POST.get(f'explicacao-{i}-{j}')
                explicacao.pontuacao = request.POST.get(f'pontuacao-{i}')
                explicacao.save()
                
        return redirect('detalhes_questionario', questionario_id)

    return render(request, 'edit_questionario.html', {
        'questionario': questionario,
        'titulo': titulo,
        'image': image,
        'explicacao': explicacao,
        'questoes': questoes,
        'alternativas': alternativas,
    })
    
def inquerito (request, questionario_id):
        questionario = get_object_or_404(Questionario, pk=questionario_id)
        return render(request, 'inquerito.html', {'questionario': questionario})
    
def submit_answers(request, questionario_id):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    questionario = get_object_or_404(Questionario, pk=questionario_id)
    answers = [request.POST.get(f'questao{questao.id}') for questao in questionario.questao_set.all()]
    total_pontuacao = sum([Alternativa.objects.get(pk=answer).pontuacao for answer in answers])
    niveis = Explicacao.objects.order_by('pontuacao')
    image = questionario.imagem
    quest_titulo = questionario.titulo

    intervals = []
    previous_pontuacao = 0
    for nivel in niveis:
        interval = (previous_pontuacao, nivel.pontuacao)
        intervals.append(interval)
        previous_pontuacao = nivel.pontuacao + 1

    explicacao = None
    nivel_correspondente = None
    for interval in intervals:
        if interval[0] <= total_pontuacao <= interval[1]:
            nivel = Explicacao.objects.get(pontuacao=interval[1])
            nivel_correspondente = Explicacao.objects.get(pontuacao=interval[1]).nivel
            explicacao = nivel.texto
            break
        else:
            nivel = Explicacao.objects.get(pontuacao=interval[1])
            nivel_correspondente = Explicacao.objects.get(pontuacao=interval[1]).nivel
            explicacao = nivel.texto

    nivel_titulo = nivel_correspondente.titulo

    context = {
        'questionario': questionario,
        'titulo': quest_titulo,
        'explicacao': explicacao,
        'total_pontuacao': total_pontuacao,
        'image': image,
        'nivel_titulo': nivel_titulo,
        'nome': nome,
        'email': email,
    }
    
    subject = f"Questionário: {quest_titulo}"
    print("subject", subject)
    message = f"Olá {nome}, você acertou {total_pontuacao} pontos e está no {nivel_titulo} do questionário {quest_titulo}."
    print("message", message)
    email_from = settings.EMAIL_HOST_USER
    print("email_from", email_from)
    recipients = [email]
    print("recipients", recipients)
    
    Email = send_mail(subject, message, email_from, recipients)
    
    return render(request, 'submit.html', {'questionario': questionario, 'context': context})
         
         

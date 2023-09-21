def submit_answers(request, questionario_id):
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
    for interval in intervals:
        if interval[0] <= total_pontuacao <= interval[1]:
            nivel = Explicacao.objects.get(pontuacao=interval[1])
            explicacao = nivel.texto
            break
        else:
            nivel = Explicacao.objects.get(pontuacao=interval[1])
            explicacao = nivel.texto

    context = {
        'questionario': questionario,
        'titulo': quest_titulo,
        'explicacao': explicacao,
        'total_pontuacao': total_pontuacao,
        'image': image,
    }
    return render(request, 'submit.html', {'questionario': questionario, 'context': context})
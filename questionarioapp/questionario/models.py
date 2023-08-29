# questionarioapp/models.py

from django.db import models

class Questionario(models.Model):
    titulo = models.CharField(max_length=100)
    explicacao = models.TextField()

class Questao(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)

class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    

    
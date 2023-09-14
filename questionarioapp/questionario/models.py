# questionarioapp/models.py

from django.db import models

class Questionario(models.Model):
    titulo = models.CharField(max_length=100)
    explicacao = models.TextField()
    imagem = models.ImageField(upload_to='media', blank=True, null=True, default=None)

class Questao(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)

class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    pontuacao = models.IntegerField(default=0)
    
class Nivel(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    
class Explicacao(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    pontuacao = models.IntegerField(default=0)
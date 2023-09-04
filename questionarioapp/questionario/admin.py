from django.contrib import admin
from .models import Questionario, Questao, Alternativa, Nivel, Explicacao

# Register your models here.
admin.site.register(Questionario)
admin.site.register(Questao)
admin.site.register(Alternativa)
admin.site.register(Nivel)
admin.site.register(Explicacao)
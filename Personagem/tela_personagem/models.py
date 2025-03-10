# personagens/models.py
from django.db import models

class Tela_personagem(models.Model):
    nome = models.CharField(max_length=30, default="")  # Valor padrão para começar
    vida = models.IntegerField(default="0")
    mana = models.IntegerField(default="0")

    vigor = models.IntegerField(default="0")
    forca = models.IntegerField(default="0")
    destreza = models.IntegerField(default="0")
    inteligencia = models.IntegerField(default="0")
    determinacao = models.IntegerField(default="0")
    perspicacia = models.IntegerField(default="0")
    carisma = models.IntegerField(default="0")

    danoFixo_1 = models.IntegerField(default="0")
    penetracao_1 = models.IntegerField(default="0")
    danoFixo_2 = models.IntegerField(default="0")
    penetracao_2 = models.IntegerField(default="0")
    danoFixo_3 = models.IntegerField(default="0")
    penetracao_3 = models.IntegerField(default="0")
    
    defesaFixa_1 = models.IntegerField(default="0")
    resistencia_1 = models.IntegerField(default="0")
    defesaFixa_2 = models.IntegerField(default="0")
    resistencia_2 = models.IntegerField(default="0")
    defesaFixa_3 = models.IntegerField(default="0")
    resistencia_3 = models.IntegerField(default="0")
    defesaFixa_4 = models.IntegerField(default="0")
    resistencia_4 = models.IntegerField(default="0")
    defesaFixa_5 = models.IntegerField(default="0")
    resistencia_5 = models.IntegerField(default="0")
    
    rolagem1 = models.IntegerField(default="0") 
    rolagem2 = models.IntegerField(default="0") 
    rolagem3 = models.IntegerField(default="0") 
    rolagem4 = models.IntegerField(default="0") 
    rolagem5 = models.IntegerField(default="0") 
    rolagem6 = models.IntegerField(default="0") 
    rolagem7 = models.IntegerField(default="0") 
    rolagem8 = models.IntegerField(default="0") 
    rolagem9 = models.IntegerField(default="0") 
    rolagem10 = models.IntegerField(default="0")    
    rolagem11 = models.IntegerField(default="0")    
    rolagem12 = models.IntegerField(default="0")    
    rolagem13 = models.IntegerField(default="0")    
    rolagem14 = models.IntegerField(default="0")    
    rolagem15 = models.IntegerField(default="0")    
    
    def __str__(self):
        return self.nome
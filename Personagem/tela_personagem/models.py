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
    
    def __str__(self):
        return self.nome
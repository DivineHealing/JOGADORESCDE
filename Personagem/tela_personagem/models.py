# personagens/models.py
from django.db import models
from base_personagem.models import Base_personagem

class Tela_personagem(models.Model):
    personagem = models.ForeignKey(Base_personagem, on_delete=models.CASCADE)

    nome = models.CharField(max_length=25, blank=True, default="")

    # ATRIBUTOS e REGENERAÇÃO
    vida = models.IntegerField(default=100, blank=True)
    mana = models.IntegerField(default=100, blank=True)
    vigor = models.IntegerField(default=100, blank=True)
    regenVida = models.IntegerField(default=100, blank=True)
    regenMana = models.IntegerField(default=100, blank=True)
    regenVigor = models.IntegerField(default=100, blank=True)

    # STATUS
    forca = models.IntegerField(default=0, blank=True)
    destreza = models.IntegerField(default=0, blank=True)
    inteligencia = models.IntegerField(default=0, blank=True)
    determinacao = models.IntegerField(default=0, blank=True)
    perspicacia = models.IntegerField(default=0, blank=True)
    carisma = models.IntegerField(default=0, blank=True)

    # STATUS PERCENTUAL
    forcaPer = models.IntegerField(default=0, blank=True)
    destrezaPer = models.IntegerField(default=0, blank=True)
    inteligenciaPer = models.IntegerField(default=0, blank=True)
    determinacaoPer = models.IntegerField(default=0, blank=True)
    perspicaciaPer = models.IntegerField(default=0, blank=True)
    carismaPer = models.IntegerField(default=0, blank=True)

    # DEFESA
    reducao = models.IntegerField(default=0, blank=True)
    defesaFixaEspiritual = models.IntegerField(default=0, blank=True)
    reducaoEspiritual = models.IntegerField(default=0, blank=True)

    # DANO
    esmagamento = models.IntegerField(default=0, blank=True)
    penExtra = models.IntegerField(default=0, blank=True)
    danoFinal = models.IntegerField(default=0, blank=True)
    espiritualPerc = models.IntegerField(default=0, blank=True)
    espiritualFixo = models.IntegerField(default=0, blank=True)
    dreno = models.IntegerField(default=0, blank=True)
    exaustao = models.IntegerField(default=0, blank=True)
    murchamento = models.IntegerField(default=0, blank=True)
    
    '''def __str__(self):
        return self.nome'''
    
class Character_attribute(models.Model):
    personagem = models.ForeignKey(Base_personagem, on_delete=models.CASCADE)
    variavelTipo = models.CharField(max_length=50, default="", blank=True)
    variavelPropriedade = models.CharField(max_length=50, default="", blank=True)
    variavelValor = models.IntegerField(default=0, blank=True)
    posicao = models.IntegerField()
    peca = models.CharField(max_length=50, default="", blank=True)
    origem = models.CharField(max_length=50, default="", blank=True)

    '''def __str__(self):
        return self.nome'''
    
class Character_effects(models.Model):
    personagem = models.ForeignKey(Base_personagem, on_delete=models.CASCADE)
    variavelTipo = models.CharField(max_length=50, default="", blank=True) # efeitoTipo
    variavelNome = models.CharField(max_length=50, default="", blank=True) # efeitoNome
    variavelDescricao = models.CharField(max_length=50, default="", blank=True) # efeitoDescricao
    posicao = models.IntegerField()
    peca = models.CharField(max_length=50, default="", blank=True)
    origem = models.CharField(max_length=50, default="", blank=True)

    '''def __str__(self):
        return self.nome'''
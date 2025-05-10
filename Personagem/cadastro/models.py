from django.db import models
from base_personagem.models import Base_personagem

class Maestria(models.Model):
    TIPO_CHOICES = [
        ('exemplar', 'Exemplar'),
        ('auxiliar', 'Auxiliar'),
        ('oficio', 'Oficio')
    ]

    peca = models.CharField(max_length=25, choices=TIPO_CHOICES, default='exemplar')

    # NOME DO PERSONAGEM
    personagem = models.ForeignKey(Base_personagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default="")

    # ATRIBUTOS e REGENERAÇÃO
    vidaBase = models.IntegerField(default=0, blank=True)
    vidaTotal = models.IntegerField(default=0, blank=True)
    regenVida = models.IntegerField(default=0, blank=True)
    mana = models.IntegerField(default=0, blank=True)
    regenMana = models.IntegerField(default=0, blank=True)
    vigor = models.IntegerField(default=0, blank=True)
    regenVigor = models.IntegerField(default=0, blank=True)

    # STATUS
    forcaPer = models.IntegerField(default=0, blank=True)
    destrezaPer = models.IntegerField(default=0, blank=True)
    inteligenciaPer = models.IntegerField(default=0, blank=True)
    determinacaoPer = models.IntegerField(default=0, blank=True)
    perspicaciaPer = models.IntegerField(default=0, blank=True)
    carismaPer = models.IntegerField(default=0, blank=True)

    # DEFESA
    reducao = models.IntegerField(default=0, blank=True)
    bloqueio = models.IntegerField(default=0, blank=True)
    aumentoDA = models.IntegerField(default=0, blank=True)
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
    
    #def __str__(self):
    #    return self.personagem
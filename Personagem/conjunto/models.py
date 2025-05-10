from django.db import models
from base_personagem.models import Base_personagem

class Conjunto(models.Model):
    TIPO_CHOICES = [
        ('conjunto', 'Conjunto'),
        ('elmo', 'Elmo'),
        ('peitoral', 'Peitoral'),
        ('manoplas', 'Manoplas'),
        ('pernas', 'Calcas'),
        ('botas', 'Bota'),
    ]

   
    peca = models.CharField(max_length=25, choices=TIPO_CHOICES, default='principal')

    # NOME DO PERSONAGEM
    personagem = models.ForeignKey(Base_personagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default="")

    # ATRIBUTOS e REGENERAÇÃO
    vida = models.IntegerField(default=0, blank=True)
    vidaBase = models.IntegerField(default=0, blank=True)
    regenVida = models.IntegerField(default=0, blank=True)
    mana = models.IntegerField(default=0, blank=True)
    regenMana = models.IntegerField(default=0, blank=True)
    vigor = models.IntegerField(default=0, blank=True)
    regenVigor = models.IntegerField(default=0, blank=True)

    # STATUS
    forca = models.IntegerField(default=0, blank=True)
    destreza = models.IntegerField(default=0, blank=True)
    inteligencia = models.IntegerField(default=0, blank=True)
    determinacao = models.IntegerField(default=0, blank=True)
    perspicacia = models.IntegerField(default=0, blank=True)
    carisma = models.IntegerField(default=0, blank=True)
    
    # DEFESA
    reducao = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    defesaFixaEspiritual = models.IntegerField(default=0, blank=True)
    reducaoEspiritual = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)

    def __str__(self):
        return self.personagem
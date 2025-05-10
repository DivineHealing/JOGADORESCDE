from django.db import models

from base_personagem.models import Base_personagem

class Acessorios(models.Model):
    TIPO_CHOICES = [
        ('anelAnelar', 'Anel_Anelar'),
        ('anelIndicador', 'Anel_Indicador'),
        ('anelMedio', 'Anel_Medio'),
        ('anelMinimo', 'Anel_Minimo'),
        ('braceleteEsquerdo', 'Bracelete_Esquerdo'),
        ('braceleteDireito', 'Bracelete_Direito'),
        ('brincoEsquerdo', 'Brinco_Esquerdo'),
        ('brincoDireito', 'Brinco_Direito'),
        ('acessorioP', 'Acessorio_Principal'),
        ('acessorioS', 'Acessorio_Secundario'),
        ('cinturao', 'Cinturao'),
    ]


    peca = models.CharField(max_length=25, choices=TIPO_CHOICES, default='principal')
    
    # NOME DO PERSONAGEM
    personagem = models.ForeignKey(Base_personagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default="")

    # ATRIBUTOS e REGENERAÇÃO
    vida = models.IntegerField(default=0, blank=True)
    vidaTotal = models.IntegerField(default=0, blank=True)
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
    
    def __str__(self):
        return self.nome
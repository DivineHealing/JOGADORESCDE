from django.db import models

class Acessorios(models.Model):
    TIPO_CHOICES = [
        ('anelAnelar', 'AnelAnelar'),
        ('anelIndicador', 'AnelIndicador'),
        ('anelMedio', 'AnelMedio'),
        ('anelMinimo', 'AnelMinimo'),
        ('braceleteEsquerdo', 'BraceleteEsquerdo'),
        ('braceleteDireito', 'BraceleteDireito'),
        ('brincoEsquerdo', 'BrincoEsquerdo'),
        ('brincoDireito', 'BrincoDireito'),
        ('acessorioP', 'AcessorioP'),
        ('acessorioS', 'AcessorioS'),
        ('cinturao', 'Cinturao'),
    ]


    personagem = models.CharField(max_length=100, default="")
    peca = models.CharField(max_length=25, choices=TIPO_CHOICES, default='anelAnelar')
    nome = models.CharField(max_length=30, default="")
    vida = models.IntegerField(default=0, blank=True)
    forca = models.IntegerField(default=0, blank=True)
    destreza = models.IntegerField(default=0, blank=True)
    inteligencia = models.IntegerField(default=0, blank=True)
    determinacao = models.IntegerField(default=0, blank=True)
    perspicacia = models.IntegerField(default=0, blank=True)
    carisma = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.nome
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

    nome = models.CharField(max_length=30, default="")  # Valor padrão para começar
    vida = models.IntegerField(default="0")
    forca = models.IntegerField(default="0")
    destreza = models.IntegerField(default="0")
    inteligencia = models.IntegerField(default="0")
    determinacao = models.IntegerField(default="0")
    perspicacia = models.IntegerField(default="0")
    carisma = models.IntegerField(default="0")
    reducao = models.IntegerField(default="0")
    danoFixo_1 = models.IntegerField(default="0")
    penetracao_1 = models.IntegerField(default="0")

    def __str__(self):
        return self.nome
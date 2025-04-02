from django.db import models

class Arma(models.Model):
    TIPO_CHOICES = [
        ('principal', 'Principal'),
        ('secundaria', 'Secundaria'),
    ]

    personagem = models.CharField(max_length=100, default="")
    peca = models.CharField(max_length=25, choices=TIPO_CHOICES, default='principal')
    nome = models.CharField(max_length=30, default="")
    vida = models.IntegerField(default=0, blank=True)
    forca = models.IntegerField(default=0, blank=True)
    destreza = models.IntegerField(default=0, blank=True)
    inteligencia = models.IntegerField(default=0, blank=True)
    determinacao = models.IntegerField(default=0, blank=True)
    perspicacia = models.IntegerField(default=0, blank=True)
    carisma = models.IntegerField(default=0, blank=True)
    danoFixo_1 = models.IntegerField(default="0")
    penetracao_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    danoFinal = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)

    def __str__(self):
        return self.nome
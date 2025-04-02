from django.db import models

class Conjunto(models.Model):
    TIPO_CHOICES = [
        ('conjunto', 'Conjunto'),
        ('elmo', 'Elmo'),
        ('peitoral', 'Peitoral'),
        ('manoplas', 'Manoplas'),
        ('pernas', 'Calcas'),
        ('botas', 'Bota'),
    ]

    personagem = models.CharField(max_length=100, default="")
    peca = models.CharField(max_length=10, choices=TIPO_CHOICES, default='elmo')
    nome = models.CharField(max_length=30, default="")
    vida = models.IntegerField(default=0, blank=True)
    forca = models.IntegerField(default=0, blank=True)
    destreza = models.IntegerField(default=0, blank=True)
    inteligencia = models.IntegerField(default=0, blank=True)
    determinacao = models.IntegerField(default=0, blank=True)
    perspicacia = models.IntegerField(default=0, blank=True)
    carisma = models.IntegerField(default=0, blank=True)
    defesaFixa_1 = models.IntegerField(default=0, blank=True)
    resistencia_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    reducao = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)

    def __str__(self):
        return self.nome
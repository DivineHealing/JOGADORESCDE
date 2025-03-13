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

    nome = models.CharField(max_length=30, default="")  # Valor padrão para começar
    vida = models.IntegerField(default="0")
    forca = models.IntegerField(default="0")
    destreza = models.IntegerField(default="0")
    inteligencia = models.IntegerField(default="0")
    determinacao = models.IntegerField(default="0")
    perspicacia = models.IntegerField(default="0")
    carisma = models.IntegerField(default="0")
    reducao = models.IntegerField(default="0")
    defesaFixa_1 = models.IntegerField(default="0")
    resistencia_1 = models.IntegerField(default="0")

    def __str__(self):
        return self.nome
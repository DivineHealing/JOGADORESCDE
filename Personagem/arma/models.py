from django.db import models

class Arma(models.Model):
    nome = models.CharField(max_length=30, default="")  # Valor padrão para começar
    forca = models.IntegerField(default="0")
    destreza = models.IntegerField(default="0")
    inteligencia = models.IntegerField(default="0")
    determinacao = models.IntegerField(default="0")
    perspicacia = models.IntegerField(default="0")
    carisma = models.IntegerField(default="0")
    danoFixo1 = models.IntegerField(default="0")

    def __str__(self):
        return self.nome
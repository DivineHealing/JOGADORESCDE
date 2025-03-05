from django.db import models

# Create your models here.
class Cadastro(models.Model):
    numero1 = models.IntegerField()
    numero2 = models.IntegerField()
    resultado = models.IntegerField()

    def __int__(self):  # descobrir para que serve retornar o resultado
        return self.resultado
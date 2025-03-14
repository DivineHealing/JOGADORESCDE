from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    # ... outros campos (ex: classe, raca, nivel, etc.)

class ConjuntoArmadura(models.Model):
    personagem = models.ForeignKey(Personagem, related_name='conjuntos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, blank=True)  # Nome do Conjunto

class PecaArmadura(models.Model):
    TIPO_CHOICES = [
        ('conjuntoEquip', 'ConjuntoEquip'),
        ('elmo', 'Elmo'),
        ('peitoral', 'Peitoral'),
        ('manoplas', 'Manoplas'),
        ('calcas', 'Calças'),
        ('botas', 'Botas'),
    ]
    #   Remova essa ForeignKey da classe abstrata.  Ela será definida nas subclasses.
    # conjunto = models.ForeignKey(ConjuntoArmadura, related_name='pecas', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=100)  # Nome da peça específica (ex: "Elmo de Aço Élfico")

    class Meta:
        abstract = True  # Classe abstrata

    # Atributos (comuns a todas as peças)
    vida = models.IntegerField(default=0)
    regenVida = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    regenMana = models.IntegerField(default=0)
    vigor = models.IntegerField(default=0)
    regenVigor = models.IntegerField(default=0)

    # Status (comuns a todas as peças)
    forca = models.IntegerField(default=0)
    destreza = models.IntegerField(default=0)
    inteligencia = models.IntegerField(default=0)
    determinacao = models.IntegerField(default=0)
    perspicacia = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)

    # Defesas (valor numérico + combinação de elementos)
    defesaFixa_1 = models.IntegerField(default=0)  # Valor numérico da defesa
    elementos_defesaFixa_1 = models.CharField(max_length=255, blank=True)  # Combinação de elementos (string)
    resistencia_1 = models.IntegerField(default=0)
    elementos_resistencia_1 = models.CharField(max_length=255, blank=True)
    # ... outras defesas ...

class ConjuntoEquip(PecaArmadura):
    conjunto = models.ForeignKey(ConjuntoArmadura, related_name='conjuntoEquip', on_delete=models.CASCADE)
    # ... campos específicos do elmo (se houver)

class Elmo(PecaArmadura):
    conjunto = models.ForeignKey(ConjuntoArmadura, related_name='elmos', on_delete=models.CASCADE)

class Peitoral(PecaArmadura):
    conjunto = models.ForeignKey(ConjuntoArmadura, related_name='peitorais', on_delete=models.CASCADE)

class Manoplas(PecaArmadura):
    conjunto = models.ForeignKey(ConjuntoArmadura, related_name='manoplas', on_delete=models.CASCADE)

class Calcas(PecaArmadura):
    conjunto = models.ForeignKey(ConjuntoArmadura, related_name='calcas', on_delete=models.CASCADE)

class Botas(PecaArmadura):
    conjunto = models.ForeignKey(ConjuntoArmadura, related_name='botas', on_delete=models.CASCADE)
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
    regenVida = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    regenMana = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    regenVigor = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)

    # STATUS
    forca = models.IntegerField(default=0, blank=True)
    destreza = models.IntegerField(default=0, blank=True)
    inteligencia = models.IntegerField(default=0, blank=True)
    determinacao = models.IntegerField(default=0, blank=True)
    perspicacia = models.IntegerField(default=0, blank=True)
    carisma = models.IntegerField(default=0, blank=True)

    # ROLAGEM
    tipoRolagem_1 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_2 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_3 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_4 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_5 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_6 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_7 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_8 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_9 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_10 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_11 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_12 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_13 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_14 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_15 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_15 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_16 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_17 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_18 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_19 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_20 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_21 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_22 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_23 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_24 = models.CharField(max_length=25, blank=True, default="")
    tipoRolagem_25 = models.CharField(max_length=25, blank=True, default="")
    rolagem_1 = models.CharField(max_length=25, blank=True, default="")
    rolagem_2 = models.CharField(max_length=25, blank=True, default="")
    rolagem_3 = models.CharField(max_length=25, blank=True, default="")
    rolagem_4 = models.CharField(max_length=25, blank=True, default="")
    rolagem_5 = models.CharField(max_length=25, blank=True, default="")
    rolagem_6 = models.CharField(max_length=25, blank=True, default="")
    rolagem_7 = models.CharField(max_length=25, blank=True, default="")
    rolagem_8 = models.CharField(max_length=25, blank=True, default="")
    rolagem_9 = models.CharField(max_length=25, blank=True, default="")
    rolagem_10 = models.CharField(max_length=25, blank=True, default="")
    rolagem_11 = models.CharField(max_length=25, blank=True, default="")
    rolagem_12 = models.CharField(max_length=25, blank=True, default="")
    rolagem_13 = models.CharField(max_length=25, blank=True, default="")
    rolagem_14 = models.CharField(max_length=25, blank=True, default="")
    rolagem_15 = models.CharField(max_length=25, blank=True, default="")
    rolagem_15 = models.CharField(max_length=25, blank=True, default="")
    rolagem_16 = models.CharField(max_length=25, blank=True, default="")
    rolagem_17 = models.CharField(max_length=25, blank=True, default="")
    rolagem_18 = models.CharField(max_length=25, blank=True, default="")
    rolagem_19 = models.CharField(max_length=25, blank=True, default="")
    rolagem_20 = models.CharField(max_length=25, blank=True, default="")
    rolagem_21 = models.CharField(max_length=25, blank=True, default="")
    rolagem_22 = models.CharField(max_length=25, blank=True, default="")
    rolagem_23 = models.CharField(max_length=25, blank=True, default="")
    rolagem_24 = models.CharField(max_length=25, blank=True, default="")
    rolagem_25 = models.CharField(max_length=25, blank=True, default="")

    # AMPLIFICAÇÃO
    elementoAmplificacao_1 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_2 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_3 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_4 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_5 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_6 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_7 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_8 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_9 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_10 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_11 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_12 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_13 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_14 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_15 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_15 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_16 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_17 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_18 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_19 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_20 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_21 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_22 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_23 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_24 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_25 = models.CharField(max_length=25, blank=True, default="")
    amplificacao_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_3 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_4 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_5 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_6 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_7 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_8 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_9 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_10 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_11 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_12 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_13 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_14 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_15 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_15 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_16 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_17 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_18 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_19 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_20 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_21 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_22 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_23 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_24 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_25 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    
    def __str__(self):
        return self.nome
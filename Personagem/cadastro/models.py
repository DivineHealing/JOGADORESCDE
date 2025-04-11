from django.db import models
from base_personagem.models import Base_personagem

class Maestria(models.Model):
    TIPO_CHOICES = [
        ('exemplar', 'Exemplar'),
        ('auxiliar', 'Auxiliar'),
        ('oficio', 'Oficio')
    ]

    peca = models.CharField(max_length=25, choices=TIPO_CHOICES, default='exemplar')

    # NOME DO PERSONAGEM
    personagem = models.ForeignKey(Base_personagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default="")

    # ATRIBUTOS e REGENERAÇÃO
    vida = models.IntegerField(default=0, blank=True)
    regenVida = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    mana = models.IntegerField(default=0, blank=True)
    regenMana = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    vigor = models.IntegerField(default=0, blank=True)
    regenVigor = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)

    # STATUS
    forca = models.IntegerField(default=0, blank=True)
    destreza = models.IntegerField(default=0, blank=True)
    inteligencia = models.IntegerField(default=0, blank=True)
    determinacao = models.IntegerField(default=0, blank=True)
    perspicacia = models.IntegerField(default=0, blank=True)
    carisma = models.IntegerField(default=0, blank=True)

    # ROLAGEM
    tipoRolagem_1 = models.CharField(max_length=100, default="")
    tipoRolagem_2 = models.CharField(max_length=100, default="")
    tipoRolagem_3 = models.CharField(max_length=100, default="")
    tipoRolagem_4 = models.CharField(max_length=100, default="")
    tipoRolagem_5 = models.CharField(max_length=100, default="")
    rolagem_1 = models.IntegerField(default=0, blank=True)
    rolagem_2 = models.IntegerField(default=0, blank=True)
    rolagem_3 = models.IntegerField(default=0, blank=True)
    rolagem_4 = models.IntegerField(default=0, blank=True)
    rolagem_5 = models.IntegerField(default=0, blank=True)

    # DEFESA
    elementoDefesa_1 = models.CharField(max_length=100, default="")
    elementoDefesa_2 = models.CharField(max_length=100, default="")
    elementoDefesa_3 = models.CharField(max_length=100, default="")
    elementoDefesa_4 = models.CharField(max_length=100, default="")
    elementoDefesa_5 = models.CharField(max_length=100, default="")
    elementoResistencia_1 = models.CharField(max_length=100, default="")
    elementoResistencia_2 = models.CharField(max_length=100, default="")
    elementoResistencia_3 = models.CharField(max_length=100, default="")
    elementoResistencia_4 = models.CharField(max_length=100, default="")
    elementoResistencia_5 = models.CharField(max_length=100, default="")
    defesaFixa_1 = models.IntegerField(default=0, blank=True)
    defesaFixa_2 = models.IntegerField(default=0, blank=True)
    defesaFixa_3 = models.IntegerField(default=0, blank=True)
    defesaFixa_4 = models.IntegerField(default=0, blank=True)
    defesaFixa_5 = models.IntegerField(default=0, blank=True)
    resistencia_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    resistencia_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    resistencia_3 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    resistencia_4 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    resistencia_5 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    reducao = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    defesaFixaEspiritual = models.IntegerField(default=0, blank=True)
    reducaoEspiritual = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)

    # DANO
    elementoDano_1 = models.CharField(max_length=100, default="")
    elementoDano_2 = models.CharField(max_length=100, default="")
    elementoDano_3 = models.CharField(max_length=100, default="")
    elementoDano_4 = models.CharField(max_length=100, default="")
    elementoDano_5 = models.CharField(max_length=100, default="")
    elementoPenetracao_1 = models.CharField(max_length=100, default="")
    elementoPenetracao_2 = models.CharField(max_length=100, default="")
    elementoPenetracao_3 = models.CharField(max_length=100, default="")
    elementoPenetracao_4 = models.CharField(max_length=100, default="")
    elementoPenetracao_5 = models.CharField(max_length=100, default="")
    danoFixo_1 = models.IntegerField(default=0, blank=True)
    danoFixo_2 = models.IntegerField(default=0, blank=True)
    danoFixo_3 = models.IntegerField(default=0, blank=True)
    danoFixo_4 = models.IntegerField(default=0, blank=True)
    danoFixo_5 = models.IntegerField(default=0, blank=True)
    penetracao_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    penetracao_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    penetracao_3 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    penetracao_4 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    penetracao_5 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    esmagamento = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    penExtra = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    danoFinal = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    espiritualPerc = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    espiritualFixo = models.IntegerField(default=0, blank=True)

    # AMPLIFICAÇÃO
    elementoAmplificacao_1 = models.CharField(max_length=100, default="")
    elementoAmplificacao_2 = models.CharField(max_length=100, default="")
    elementoAmplificacao_3 = models.CharField(max_length=100, default="")
    elementoAmplificacao_4 = models.CharField(max_length=100, default="")
    elementoAmplificacao_5 = models.CharField(max_length=100, default="")
    amplificacao_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_3 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_4 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_5 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)

    def __str__(self):
        return self.personagem
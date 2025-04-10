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
    rolagem_1 = models.CharField(max_length=25, blank=True, default="")
    rolagem_2 = models.CharField(max_length=25, blank=True, default="")
    rolagem_3 = models.CharField(max_length=25, blank=True, default="")
    rolagem_4 = models.CharField(max_length=25, blank=True, default="")
    rolagem_5 = models.CharField(max_length=25, blank=True, default="")

    # DEFESA
    elementoDefesa_1 = models.CharField(max_length=100, default="", blank=True)
    elementoDefesa_2 = models.CharField(max_length=100, default="", blank=True)
    elementoDefesa_3 = models.CharField(max_length=100, default="", blank=True)
    elementoDefesa_4 = models.CharField(max_length=100, default="", blank=True)
    elementoDefesa_5 = models.CharField(max_length=100, default="", blank=True)
    elementoResistencia_1 = models.CharField(max_length=100, default="", blank=True)
    elementoResistencia_2 = models.CharField(max_length=100, default="", blank=True)
    elementoResistencia_3 = models.CharField(max_length=100, default="", blank=True)
    elementoResistencia_4 = models.CharField(max_length=100, default="", blank=True)
    elementoResistencia_5 = models.CharField(max_length=100, default="", blank=True)
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
    elementoDano_1 = models.CharField(max_length=100, default="", blank=True)
    elementoDano_2 = models.CharField(max_length=100, default="", blank=True)
    elementoDano_3 = models.CharField(max_length=100, default="", blank=True)
    elementoDano_4 = models.CharField(max_length=100, default="", blank=True)
    elementoDano_5 = models.CharField(max_length=100, default="", blank=True)
    elementoPenetracao_1 = models.CharField(max_length=100, default="", blank=True)
    elementoPenetracao_2 = models.CharField(max_length=100, default="", blank=True)
    elementoPenetracao_3 = models.CharField(max_length=100, default="", blank=True)
    elementoPenetracao_4 = models.CharField(max_length=100, default="", blank=True)
    elementoPenetracao_5 = models.CharField(max_length=100, default="", blank=True)
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
    elementoAmplificacao_1 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_2 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_3 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_4 = models.CharField(max_length=25, blank=True, default="")
    elementoAmplificacao_5 = models.CharField(max_length=25, blank=True, default="")
    amplificacao_1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_3 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_4 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    amplificacao_5 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, blank=True)
    
    def __str__(self):
        return self.personagem
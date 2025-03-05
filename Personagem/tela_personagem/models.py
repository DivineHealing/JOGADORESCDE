# personagens/models.py
from django.db import models

class Tela_personagem(models.Model):
    nome = models.CharField(max_length=200, default="Aryah Astaris")  # Valor padrão para começar
    vida = models.CharField(max_length=50, default="307.481 [614.962]")
    mana = models.CharField(max_length=50, default="135 [243]")
    vigor = models.CharField(max_length=50, default="125 [225]")
    forca = models.CharField(max_length=50, default="650 +6")
    destreza = models.CharField(max_length=50, default="650 +6")
    inteligencia = models.CharField(max_length=50, default="3.000 +40")
    determinacao = models.CharField(max_length=50, default="10.062 +100")
    perspicacia = models.CharField(max_length=50, default="2.710 +27")
    carisma = models.CharField(max_length=50, default="1.821 +18")
    dano_fixo_solar = models.CharField(max_length=50, default="154.324")
    penetracao_solar = models.CharField(max_length=50, default="90%")
    dano_fixo_sacrosolar = models.CharField(max_length=50, default="20")
    dano_final = models.CharField(max_length=50, default="10%")
    defesa_fixa_chaos = models.CharField(max_length=50, default="10.000")
    resistencia_chaos = models.CharField(max_length=50, default="90%")
    defesa_fixa_espiritual = models.CharField(max_length=50, default="1.150")
    reducao_espiritual = models.CharField(max_length=50, default="60%")
    resistencia_necrotica = models.CharField(max_length=50, default="25%")
    rolagem_invocacao = models.CharField(max_length=50, default="10")
    rolagem_cura = models.CharField(max_length=50, default="10")
    rolagem_curado = models.CharField(max_length=50, default="10")
    rolagem_aprimoramento = models.CharField(max_length=50, default="10")
    rolagem_magias_solares = models.CharField(max_length=50, default="10")
    rolagem_magias_diversas = models.CharField(max_length=50, default="10")
    amplificacao_solar = models.CharField(max_length=50, default="10")
    amplificacao_sacrosolar = models.CharField(max_length=50, default="10")
    suporte = models.CharField(max_length=50, default="Suporte")
    amplificacao_cura = models.CharField(max_length=50, default="10")
    amplificacao_escudo = models.CharField(max_length=50, default="10")
    amplificacao_aprimoramento = models.CharField(max_length=50, default="10")
    amplificacao_debilidades = models.CharField(max_length=50, default="10")
    cavalheiras = models.CharField(max_length=50, default="Cavalheiras")
    amplificacao_invocacao = models.CharField(max_length=50, default="10")
    reducao_murchamento_vital = models.CharField(max_length=50, default="5%")
    
    def __str__(self):
        return self.nome
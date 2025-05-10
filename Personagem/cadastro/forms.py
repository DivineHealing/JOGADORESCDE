from django import forms
from .models import Maestria

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Maestria
        fields = [
    'peca',

    # NOME DO PERSONAGEM
    'personagem',
    'nome',
    
    # ATRIBUTOS e REGENERAÇÃO
    'vidaBase',
    'vidaTotal',
    'regenVida',
    'mana',
    'regenMana',
    'vigor',
    'regenVigor',

    # STATUS
    'forcaPer',
    'destrezaPer',
    'inteligenciaPer',
    'determinacaoPer',
    'perspicaciaPer',
    'carismaPer',

    # DEFESA
    'reducao',
    'bloqueio',
    'aumentoDA',
    'reducaoEspiritual',

    # DANO
    'esmagamento',
    'penExtra',
    'danoFinal',
    'espiritualPerc',
    'espiritualFixo',
    'dreno',
    'exaustao',
    'murchamento'
]
    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
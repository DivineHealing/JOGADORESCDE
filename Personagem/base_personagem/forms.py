from django import forms
from .models import Base_personagem as Base

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class BaseForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = [
    'vida',
    'vidaBase',
    'regenVida',
    'mana',
    'regenMana',
    'vigor',
    'regenVigor',

    # STATUS
    'forca',
    'destreza',
    'inteligencia',
    'determinacao',
    'perspicacia',
    'carisma',

    # STATUS PERCENTUAL
    'forcaPer',
    'destrezaPer',
    'inteligenciaPer',
    'determinacaoPer',
    'perspicaciaPer',
    'carismaPer',

    # DEFESA
    'reducao',
    'defesaFixaEspiritual',
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
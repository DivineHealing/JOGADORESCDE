from django import forms
from .models import Conjunto
# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Conjunto
        fields = [
    'peca',
    'nome',
    'vida',
    'vidaBase',
    'regenVida',
    'mana',
    'regenMana',
    'vigor',
    'regenVigor',
    'forca',
    'destreza',
    'inteligencia',
    'determinacao',
    'perspicacia',
    'carisma',
    'forcaPer',
    'destrezaPer',
    'inteligenciaPer',
    'determinacaoPer',
    'perspicaciaPer',
    'carismaPer',
    'reducao',
    'defesaFixaEspiritual',
    'reducaoEspiritual'
]
    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
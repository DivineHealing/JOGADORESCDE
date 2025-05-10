from django import forms
from .models import Acessorios

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Acessorios
        fields = [
    'peca',
    
    # NOME DO PERSONAGEM
    'nome',

    # ATRIBUTOS e REGENERAÇÃO
    'vida',
    'vidaTotal',
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
    'carismaPer'
    ]

    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
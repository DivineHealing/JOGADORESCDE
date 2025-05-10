from django import forms
from .models import Acessorios

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Acessorios
        fields = [
'peca',
'personagem',
'regenVida',
'regenMana',
'regenVigor',
'forca',
'destreza',
'inteligencia',
'determinacao',
'perspicacia',
'carisma',
]

    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
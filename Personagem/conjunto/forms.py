from django import forms
from .models import Conjunto
# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Conjunto
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
'reducao',
'defesaFixaEspiritual',
'reducaoEspiritual'
]
    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
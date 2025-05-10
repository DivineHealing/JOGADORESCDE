from django import forms
from .models import Arma

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Arma
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
'reducaoEspiritual',
'esmagamento',
'penExtra',
'danoFinal',
'espiritualPerc',
'espiritualFixo',
]
    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
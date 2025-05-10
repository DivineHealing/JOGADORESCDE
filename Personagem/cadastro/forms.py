from django import forms
from .models import Maestria

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Maestria
        fields = [
'peca',
'personagem',
'regenVida',
'regenMana',
'regenVigor',
'forcaPer',
'destrezaPer',
'inteligenciaPer',
'determinacaoPer',
'perspicaciaPer',
'carismaPer',
'reducao',
'vidaAtual',
'reducaoEspiritual',
'esmagamento',
'penExtra',
'aumentoDA',
'espiritualPerc',
'vidaBase',
]
    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
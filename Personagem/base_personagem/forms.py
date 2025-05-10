from django import forms
from .models import Base_personagem as Base

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class BaseForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = [
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
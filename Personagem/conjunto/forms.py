from django import forms
from .models import Conjunto
# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Conjunto
        fields = ['nome', 'vida', 'forca', 'destreza', 'inteligencia', 'determinacao', 'perspicacia', 'carisma', 'reducao', 'defesaFixa_1', 'resistencia_1']  # Adicione os campos do seu modelo

    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
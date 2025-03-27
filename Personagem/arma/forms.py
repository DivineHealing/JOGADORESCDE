from django import forms
from .models import Arma

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Arma
        fields = ['nome', 'vida', 'forca', 'destreza', 'inteligencia', 'determinacao', 'perspicacia', 'carisma', 'reducao', 'danoFixo_1', 'penetracao_1']  # Adicione os campos do seu modelo

    widgets = {
        'tipo': forms.HiddenInput(), #Oculta o campo, pois já será preenchido
    }
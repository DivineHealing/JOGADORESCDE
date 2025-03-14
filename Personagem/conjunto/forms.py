from django import forms
from .models import Conjunto, Peca, TipoPeca

class ConjuntoForm(forms.ModelForm):
    class Meta:
        model = Conjunto
        fields = '__all__'  # Ou especifique os campos: ['nome', 'raridade', 'descricao']

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        exclude = ['conjunto']  # O conjunto será definido na view
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}), # Select para o tipo de peça
            'efeitos_especiais': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'class': 'form-control'}), #Text area para efeitos especiais
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
             if field_name != 'tipo':  # Já adicionamos a classe ao widget 'tipo' acima
                field.widget.attrs['class'] = 'form-control'
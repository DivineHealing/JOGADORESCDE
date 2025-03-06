from django import forms

# AQUI VAI CRIAR OS INPUTS DENTRO DO HTML

class ArmaForm(forms.Form):
    numero1 = forms.IntegerField(label="Forca", required=True)
    numero2 = forms.IntegerField(label="Destreza", required=True)
    numero3 = forms.IntegerField(label="Inteligencia", required=True)
    numero4 = forms.IntegerField(label="Determinação", required=True)
    numero5 = forms.IntegerField(label="Perspicácia", required=True)
    numero6 = forms.IntegerField(label="Carisma", required=True)

    # AQUI VAI SER PARA CHAMAR FUNÇÃO ONINPUT DO HTML
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(1, 7):
            self.fields["numero"+str(i)].widget.attrs.update({'value': 0, 'id': 'numero'+str(i)}) # Adiciona oninput ao campo numero1
            

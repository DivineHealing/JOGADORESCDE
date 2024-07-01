from dataclasses import dataclass


@dataclass
class Atributos():
    forca: float = 0
    destreza: float = 0
    inteligencia: float = 0
    determinacao: float = 0
    percepcao: float = 0
    carisma: float = 0

    def pegaValor(self, escolha:str):
        if escolha.lower() == 'forca':
            return self.forca
        if escolha.lower() == 'destreza':
            return self.destreza
        if escolha.lower() == 'inteligencia':
            return self.inteligencia
        if escolha.lower() == 'determinacao':
            return self.determinacao
        if escolha.lower() == 'percepcao':
            return self.percepcao
        if escolha.lower() == 'carisma':
            return self.carisma 

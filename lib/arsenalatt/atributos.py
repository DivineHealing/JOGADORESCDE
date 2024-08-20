from dataclasses import dataclass


@dataclass
class Atributos():
    forca: float = 0  # necessario colocar todos esse valores para pegar a classe
    destreza: float = 0
    inteligencia: float = 0
    determinacao: float = 0
    percepcao: float = 0
    carisma: float = 0

    def pegaValor(self, escolha:str):  # Ira retornar o valor do atributo escolhido
        return getattr(self, escolha)
from dataclasses import dataclass

@dataclass
class Elementos:
    tipo1: float
    tipo2: float = 0
    tipo3: float = 0

    def pegaTipo(self, escolha:str):  # Ira retornar o valor do atributo escolhido
        return getattr(self, escolha)
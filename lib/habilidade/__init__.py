from lib.atributos import Atributos
from dataclasses import dataclass

@dataclass 
class Habilidade:  # Modficiar futuramente caso precisar separar habilidades passivas de ativas
    att: Atributos
    attp: Atributos
    #primaria: bool = true
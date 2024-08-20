from .atributos import Atributos
from dataclasses import dataclass, field

@dataclass 
class Habilidade:  # Modficiar futuramente caso precisar separar habilidades passivas de ativas
    att: Atributos = field(default_factory=Atributos)
    attp: Atributos = field(default_factory=Atributos)
    #primaria: bool = true
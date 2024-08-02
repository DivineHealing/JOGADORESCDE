from lib.atributos import Atributos
from dataclasses import dataclass, field

@dataclass
class Raca:
    attp: Atributos = field(default_factory=Atributos)
    
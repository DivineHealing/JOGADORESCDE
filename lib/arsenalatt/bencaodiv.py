from .atributos import Atributos
from dataclasses import dataclass, field

@dataclass
class BencaoDiv:
    attp: Atributos = field(default_factory=Atributos)
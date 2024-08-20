from .atributos import Atributos
from dataclasses import dataclass, field

@dataclass
class BonusEx:
    att: Atributos = field(default_factory=Atributos)
    attp: Atributos = field(default_factory=Atributos)
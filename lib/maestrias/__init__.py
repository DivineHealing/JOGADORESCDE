from lib.atributos import Atributos
from dataclasses import dataclass, field

@dataclass
class Maestrias:
    att: Atributos = field(default_factory=Atributos)
    attp: Atributos = field(default_factory=Atributos)
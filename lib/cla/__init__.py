from lib.atributos import Atributos
from dataclasses import dataclass, field

@dataclass
class Cla:
    att: Atributos = field(default_factory=Atributos)
    attp: Atributos = field(default_factory=Atributos)
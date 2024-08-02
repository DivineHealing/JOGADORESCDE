from lib.atributos import Atributos
from dataclasses import dataclass, field

@dataclass
class Missoes:
    att: Atributos = field(default_factory=Atributos)
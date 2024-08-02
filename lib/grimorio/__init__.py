from lib.atributos import Atributos
from dataclasses import dataclass, field

@dataclass
class Grimorio:
    attp: Atributos = field(default_factory=Atributos)
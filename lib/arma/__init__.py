from dataclasses import dataclass
from lib.atributos import Atributos

@dataclass
class Arma:
    att: Atributos
    principal: bool = True
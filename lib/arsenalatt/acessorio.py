from dataclasses import dataclass, field
from .atributos import Atributos

@dataclass
class Acessorio():
    att: Atributos = field(default_factory=Atributos) #ira pegar as informações da classe atributos
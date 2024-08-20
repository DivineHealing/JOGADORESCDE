from dataclasses import dataclass, field
from .atributos import Atributos
from .elementos import Elementos

@dataclass
class Arma:
    att: Atributos = field(default_factory=Atributos)
    principal: bool = True
    pen: Elementos = field(default_factory=Elementos)
    ampl: Elementos = field(default_factory=Elementos)
    dafixo: Elementos = field(default_factory=Elementos)
    aumfixo: Elementos = field(default_factory=Elementos)
    esmagamento: float = 0

    def pegaInfo(self, escolha):
        return getattr(self, escolha)
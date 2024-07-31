from dataclasses import dataclass
from lib.atributos import Atributos
from lib.elementos import Elementos

@dataclass
class Arma:
    att: Atributos
    principal: bool = True
    pen: Elementos = None
    ampl: Elementos = None
    dafixo: Elementos = None
    aumfixo: Elementos = None
    esmagamento: float = 0

    def pegaInfo(self, escolha):
        return getattr(self, escolha)
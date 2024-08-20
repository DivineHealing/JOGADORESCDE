from dataclasses import dataclass, field
from .maestrias import Maestrias

@dataclass
class Conjmaestria:
    principal: Maestrias = field(default_factory=Maestrias)
    secundaria: Maestrias = field(default_factory=Maestrias)
    utilitaria: Maestrias = field(default_factory=Maestrias)

    def somarMaes(self, tipo, escolha):
        if 'f' in tipo:
            total = self.principal.att.pegaValor(escolha) + self.secundaria.att.pegaValor(escolha) + self.utilitaria.att.pegaValor(escolha)
        else:
            total = self.principal.attp.pegaValor(escolha) + self.secundaria.attp.pegaValor(escolha) + self.utilitaria.attp.pegaValor(escolha)
        return total
from dataclasses import dataclass
from lib.maestrias import Maestrias

@dataclass
class Conjmaestria:
    principal: Maestrias
    secundaria: Maestrias
    utilitaria: Maestrias

    def somarMaes(self, tipo, escolha):
        if 'f' in tipo:
            total = self.principal.att.pegaValor(escolha) + self.secundaria.att.pegaValor(escolha) + self.utilitaria.att.pegaValor(escolha)
        else:
            total = self.principal.attp.pegaValor(escolha) + self.secundaria.attp.pegaValor(escolha) + self.utilitaria.attp.pegaValor(escolha)
        return total
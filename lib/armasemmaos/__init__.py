from dataclasses import dataclass
from lib.arma import Arma

@dataclass
class ArmasEmMaos:
    principal: Arma
    secundaria: Arma

    def somarArmaAtt(self, escolha):
        total = self.principal.att.pegaValor(escolha) + self.secundaria.att.pegaValor(escolha)
        return total
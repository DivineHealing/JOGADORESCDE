from dataclasses import dataclass
from lib.arma import Arma

@dataclass
class ArmasEmMaos:
    principal: Arma
    secundaria: Arma

    def somarArmaAtt(self, escolha):
        total = self.principal.att.pegaValor(escolha) + self.secundaria.att.pegaValor(escolha)
        return total
    
    def somarEspe(self, escolha1, escolha2): #vai selecionar qual informação vai pegar e qual tipo de elemento vai pegar e somara eles
        total = self.principal.pegaInfo(escolha1).pegaTipo(escolha2) + self.secundaria.pegaInfo(escolha1).pegaTipo(escolha2)
        return total
from dataclasses import dataclass, field
from .arma import Arma

@dataclass
class ArmasEmMaos:
    principal: Arma = field(default_factory=Arma)
    secundaria: Arma = field(default_factory=Arma)
    
    def somarArmaAtt(self, escolha):
        total = self.principal.att.pegaValor(escolha) + self.secundaria.att.pegaValor(escolha)
        return total
    
    def somarEspe(self, escolha1, escolha2 = None): #vai selecionar qual informação vai pegar e qual tipo de elemento vai pegar e somara eles
        if escolha2 != None:  
            total = self.principal.pegaInfo(escolha1).pegaTipo(escolha2) + self.secundaria.pegaInfo(escolha1).pegaTipo(escolha2)
        else:  # se a escolha 1 for uma variavel primitiva logo não tera uma classe (esmagamento)
            total = self.principal.pegaInfo(escolha1) + self.secundaria.pegaInfo(escolha1)
        return total
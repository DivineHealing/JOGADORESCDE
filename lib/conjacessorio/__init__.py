from dataclasses import dataclass
from lib.acessorio import Acessorio

@dataclass
class ConjAcessorio:
    anel1: Acessorio
    anel2: Acessorio
    anel3: Acessorio
    anel4: Acessorio
    bracd: Acessorio #Bracedeira Direita
    brace: Acessorio #Bracedeira Esquerda
    brind: Acessorio #Brinco Direito
    brine: Acessorio #Brinco Esquerdo
    colar: Acessorio # Colar
    capa: Acessorio #Capa ou opta por colar
    cint: Acessorio


    def somarAces(self, escolha):  # pegara o total do atributo escolhido em todos os equipamentos
        total = (self.anel1.att.pegaValor(escolha) + self.anel2.att.pegaValor(escolha) + self.anel3.att.pegaValor(escolha) + self.anel4.att.pegaValor(escolha) +
                 self.bracd.att.pegaValor(escolha) + self.brace.att.pegaValor(escolha) + self.brind.att.pegaValor(escolha) + self.brine.att.pegaValor(escolha)+
                 self.colar.att.pegaValor(escolha) + self.cint.att.pegaValor(escolha))
        return total
from dataclasses import dataclass, field
from .acessorio import Acessorio

@dataclass
class ConjAcessorio:
    anel1: Acessorio = field(default_factory=Acessorio)
    anel2: Acessorio = field(default_factory=Acessorio)
    anel3: Acessorio = field(default_factory=Acessorio)
    anel4: Acessorio = field(default_factory=Acessorio)
    bracd: Acessorio = field(default_factory=Acessorio) #Bracedeira Direita
    brace: Acessorio = field(default_factory=Acessorio) #Bracedeira Esquerda
    brind: Acessorio = field(default_factory=Acessorio) #Brinco Direito
    brine: Acessorio = field(default_factory=Acessorio) #Brinco Esquerdo
    colar: Acessorio = field(default_factory=Acessorio) # Colar
    capa: Acessorio = field(default_factory=Acessorio) #Capa ou opta por colar
    cint: Acessorio = field(default_factory=Acessorio)


    def somarAces(self, escolha):  # pegara o total do atributo escolhido em todos os equipamentos
        total = (self.anel1.att.pegaValor(escolha) + self.anel2.att.pegaValor(escolha) + self.anel3.att.pegaValor(escolha) + self.anel4.att.pegaValor(escolha) +
                 self.bracd.att.pegaValor(escolha) + self.brace.att.pegaValor(escolha) + self.brind.att.pegaValor(escolha) + self.brine.att.pegaValor(escolha)+
                 self.colar.att.pegaValor(escolha) + self.capa.att.pegaValor(escolha) + self.cint.att.pegaValor(escolha))
        return total
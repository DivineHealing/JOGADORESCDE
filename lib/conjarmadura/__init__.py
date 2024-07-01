from dataclasses import dataclass
from lib.equipamentos import Equipamento

@dataclass
class ConjArmadura:
    elmo: Equipamento
    peitoral: Equipamento
    luva: Equipamento
    calca: Equipamento
    bota: Equipamento

    def somarEquip(self, escolha):
        total = (self.elmo.att.pegaValor(escolha) + self.peitoral.att.pegaValor(escolha) + self.luva.att.pegaValor(escolha) + self.calca.att.pegaValor(escolha) + 
                 self.bota.att.pegaValor(escolha))
        return total
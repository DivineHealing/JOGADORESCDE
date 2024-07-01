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
        total = (self.elmo.pegaValor(escolha) + self.peitoral.pegaValor(escolha) + self.luva.pegaValor(escolha) + self.calca.pegaValor(escolha) + 
                 self.bota.pegaValor(escolha))
        return total
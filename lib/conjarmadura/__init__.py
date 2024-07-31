from dataclasses import dataclass
from lib.equipamentos import Equipamento

@dataclass
class ConjArmadura:
    elmo: Equipamento
    peitoral: Equipamento
    luva: Equipamento
    calca: Equipamento
    bota: Equipamento

    def somarEquip(self, escolha1, escolha2 ):  # pegara o total do atributo escolhido em todos os equipamentos       
        total = (self.elmo.pegaInfo(escolha1).pegaTipo(escolha2) + self.peitoral.pegaInfo(escolha1).pegaTipo(escolha2) + 
                 self.luva.pegaInfo(escolha1).pegaTipo(escolha2) + self.calca.pegaInfo(escolha1).pegaTipo(escolha2) + 
                 self.bota.pegaInfo(escolha1).pegaTipo(escolha2))
        return total
from dataclasses import dataclass
from lib.atributos import Atributos
from lib.elementos import Elementos

@dataclass
class Equipamento():
    att: Atributos #ira pegar as informações da classe atributos
    defe: Elementos = None  # defesa
    res: Elementos = None # resistencia
    red: Elementos = None # redução

    def pegaInfo(self, escolha):
        return getattr(self, escolha)
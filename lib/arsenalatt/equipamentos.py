from dataclasses import dataclass, field
from .atributos import Atributos
from .elementos import Elementos

@dataclass
class Equipamento():
    att: Atributos = field(default_factory=Atributos) #ira pegar as informações da classe atributos
    defe: Elementos = field(default_factory=Elementos)  # defesa
    res: Elementos = field(default_factory=Elementos) # resistencia
    red: Elementos = field(default_factory=Elementos) # redução

    def pegaInfo(self, escolha):
        return getattr(self, escolha)
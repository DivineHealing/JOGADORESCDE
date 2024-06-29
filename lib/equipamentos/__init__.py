from lib.atributos import atributos
from dataclasses import dataclass

@dataclass
class Equipamento(): #teste apenas
    ativado: bool = False
    bonusdeconjunto: Int = 0
    att: atributos = atributos()


from tela_personagem.models import Tela_personagem, Elementos_personagem
from conjunto.models import Conjunto
from base_personagem.models import Base_personagem
from arma.models import Arma
from acessorios.models import Acessorios

def criar_personagem_completo(nome_personagem: str):
    Tela_personagem.objects.create(personagem= nome_personagem)
    Elementos_personagem.objects.create(personagem= nome_personagem)
    Conjunto.objects.create(personagem= nome_personagem)
    Base_personagem.objects.create(personagem= nome_personagem)
    Arma.objects.create(personagem= nome_personagem)
    Acessorios.objects.create(personagem= nome_personagem)
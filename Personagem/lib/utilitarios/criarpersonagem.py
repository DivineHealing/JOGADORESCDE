from tela_personagem.models import Tela_personagem, nome
from conjunto.models import Conjunto
from base_personagem.models import Base_personagem
from arma.models import Arma
from acessorios.models import Acessorios
from habilidade.models import Habilidade
from cadastro.models import Maestria


def criar_personagem_completo(nome_personagem: str):
    conj_escolhas = Conjunto.TIPO_CHOICES
    arma_escolhas = Arma.TIPO_CHOICES
    aces_escolhas = Acessorios.TIPO_CHOICES
    maes_escolhas = Maestria.TIPO_CHOICES
    origens = ["base", "tela_p", "conj", "arma", "aces", "maes"]
    base_instance =  Base_personagem.objects.create(personagem= nome_personagem)
    Tela_personagem.objects.create(personagem = base_instance)  # criando tabela da tela personagem
    Habilidade.objects.create(personagem = base_instance)
    for tabela, conteudo in conj_escolhas:  # iterando a quantidade de equipamentos no conjunto
        # criando tabelas dos equipamento do conjunto ja esta nomeando a peça como comum e designando o slot da peça 
        Conjunto.objects.create(personagem = base_instance, peca= tabela, nome= conteudo + ' comum') 
    for tabela, conteudo in arma_escolhas: 
        Arma.objects.create(personagem = base_instance, peca= tabela, nome='Arma ' + conteudo)
    for tabela, conteudo in aces_escolhas: 
        Acessorios.objects.create(personagem = base_instance, peca= tabela, nome= conteudo + ' comum')
    for tabela, conteudo in maes_escolhas:
        Maestria.objects.create(personagem= base_instance, peca= tabela, nome= 'Maestria ' + conteudo)
    
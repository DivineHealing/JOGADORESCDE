from tela_personagem.models import Tela_personagem, Elementos_personagem
from conjunto.models import Conjunto
from base_personagem.models import Base_personagem
from arma.models import Arma
from acessorios.models import Acessorios
from habilidade.models import Habilidade

def criar_personagem_completo(nome_personagem: str):
    base_instance =  Base_personagem.objects.create(personagem= nome_personagem)
    Tela_personagem.objects.create(personagem = base_instance)  # criando tabela da tela personagem
    Elementos_personagem.objects.create(personagem = base_instance)  # criando tabela elemento personagem
    Habilidade.objects.create(personagem = base_instance)
    for tabela, conteudo in Conjunto.TIPO_CHOICES:  # iterando a quantidade de equipamentos no conjunto
        # criando tabelas dos equipamento do conjunto ja esta nomeando a peça como comum e designando o slot da peça 
        Conjunto.objects.create(personagem = base_instance, peca= tabela, nome= conteudo + ' comum') 
    for tabela, conteudo in Arma.TIPO_CHOICES: 
        Arma.objects.create(personagem = base_instance, peca= tabela, nome='Arma ' + conteudo)
    for tabela, conteudo in Acessorios.TIPO_CHOICES: 
        Acessorios.objects.create(personagem = base_instance, peca= tabela, nome= conteudo + ' comum')
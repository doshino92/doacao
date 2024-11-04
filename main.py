import controlador_animal
import controlador_animal
from doador import Doador
from animal import Animal
from doacao import Doacao
from adocao import Adocao
from adotante import Adotante
from ong import Ong
from moradia import Moradia


# # criando adotantes
# adotante1 = Adotante('Marcos', '11221643606','Florianópolis',1992,9,19, Moradia.CASA,False,False)
# adotante2 = Adotante('Val', '333111333','Sao Jose',2010,2,13,Moradia.CASA,False,False)
# adotante3 = Adotante('Carol', '331345611333','Sao Jose',2000,2,13,Moradia.APARTAMENTO,False, False)
#
# #criando animais
# animal1 = Animal('Mia','123', 'Viralata','Pequeno', True, True, True,'20-02-2022',
#                  '20-02-2022','20-02-2022')
# animal2 = Animal('Cagão','456', 'Pastor Alemão','Pequeno', True, True, True,'20-02-2022',
#                  '20-02-2022','20-02-2022')
# animal3 = Animal('Pitu','789', 'Tigre','Grande', True, True, True,'20-02-2022',
#                  '20-02-2022','20-02-2022')
#
# # criando doadores
# doador1 = Doador('Marcos', '11221643606', 'Trindade', 1992, 12, 17, animal1)
# doador2 = Doador('Guilherme', '1122321643606', 'Floripa', 1990, 11, 19, animal2)
# doador3 = Doador('Carla', '112216331143606', 'Floripa', 1990, 11, 19, animal3)
#
#
#
# #criando doações que recebem objetos da classe Animal e Doador
# doacao1 = Doacao(2001, 12, 19,animal1, doador1,'Caga muito' )
# doacao2 = Doacao(2022, 2, 14,animal2, doador2,'Violento' )
# doacao3 = Doacao(2021, 2, 14, animal3, doador3, 'Violento')
#
# #criando adocões que recebem objetos da classe Animal e Adotante
# adocao1 = Adocao(2023,10,15,animal1, adotante1, doador1,True)
# adocao2 = Adocao(2022,2,28,animal2, adotante2, doador2,True)
# adocao3 = Adocao(2021,2,28,animal3, adotante3, doador3,True)
#
#
# #criando uma lista de animais, doações e adoções
# lista_animais = [animal1,animal2, animal3]
# lista_doacoes = [doacao1,doacao2,doacao3]
# lista_adocoes = [adocao1,adocao2,adocao3]
#
# # criando uma instancia de ong e passando  as listas de Animais, Doacoes e Adocoes
# ong = Ong(lista_animais, lista_doacoes, lista_adocoes)
#
# #criando registro de Doação na ONG, passando doação e animal
# ong.registrar_doacao(doacao1)
# ong.registrar_doacao(doacao2)
# ong.registrar_doacao(doacao3)
#
# #criando registros de Adoação na ONG, passando adoação e animal
# ong.registrar_adocao(adocao1)
# ong.registrar_adocao(adocao2)
# ong.registrar_adocao(adocao3)
#
# #listando doacoes por periodo
# ong.doacoes_por_periodo('01-01-2000', '31-12-2024')
# ong.adocoes_por_periodo('01-01-2000', '31-12-2024')
#
# #mostrando os animais disponíveis para Doção
# ong.animais_disponiveis()
controlador_animal.abre_tela()



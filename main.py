from doador import Doador
from animal import Animal
from doacao import Doacao
from adocao import Adocao
from adotante import Adotante
from ong import Ong

# criando adotantes
adotante1 = Adotante('Marcos', '11221643606','Florianópolis',1992,9,19, True, False )
adotante2 = Adotante('Val', '333111333','Sao Jose',2000,2,13, True, False )
adotante3 = Adotante('Carol', '331345611333','Sao Jose',2000,2,13, True, False )

# criando doadores
doador1 = Doador('Marcos', '11221643606', 'Trindade', 1992, 12, 17,None)
doador2 = Doador('Guilherme', '1122321643606', 'Floripa', 1990, 11, 19,None)
doador3 = Doador('Carla', '112216331143606', 'Floripa', 1990, 11, 19,None)

#criando animais
animal1 = Animal("Mia", "Viralata", "Raiva")
animal2 = Animal("Cagão", "Pastor Alemão","V8")
animal3 = Animal("Pitu", "Tigre","V8")

#criando doações que recebem objetos da classe Animal e Doador
doacao1 = Doacao(1992, 12, 19,animal1, doador1,'Caga muito' )
doacao2 = Doacao(2022, 2, 14,animal2, doador2,'Violento' )
doacao3 = Doacao(2021, 2, 14, animal3, doador3, 'Violento')

#criando adocões que recebem objetos da classe Animal e Adotante
adocao1 = Adocao(2023,10,15,animal1, adotante1, doador1,True)
adocao2 = Adocao(2022,2,28,animal2, adotante2, doador2,True)
adocao3 = Adocao(2021,2,28,animal3, adotante3, doador3,True)

#criando uma lista de animais, doações e adoções
lista_animais = [animal1,animal2, animal3]
lista_doacoes = [doacao1,doacao2,doacao3]
lista_adocoes = [adocao1,adocao2,adocao3]

# criando uma instancia de ong e passando  as listas de Animais, Doacoes e Adocoes
ong = Ong(lista_animais, lista_doacoes, lista_adocoes)

#criando registro de Doação na ONG, passando doação e animal
ong.registrar_doacao(doacao1)
ong.registrar_doacao(doacao2)
ong.registrar_doacao(doacao3)

#criando registros de Adoação na ONG, passando adoação e animal
ong.registrar_adocao(adocao1)
ong.registrar_adocao(adocao2)

ong.doacoes_por_periodo('01-01-2000', '31-12-2024')
ong.adocoes_por_periodo("01-01-2021", "31-12-2022")

#mostrando os animais disponíveis para Doção
ong.animais_disponiveis()
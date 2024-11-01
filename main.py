from doador import Doador
from animal import Animal
from doacao import Doacao
from adocao import Adocao
from adotante import Adotante
from ong import Ong

# criando adotantes
adotante1 = Adotante('Gui', '11221643606','Florianópolis',1992,9,19, True, False )
adotante2 = Adotante('Val', '11221643606','Sao Jose',2000,2,13, True, False )

# criando doadores
doador1 = Doador('Rafaela', '11221643606', 'Trindade', 1992, 12, 17,None)
doador2 = Doador('Guilherme', '11221643606', 'Floripa', 1990, 11, 19,None)

#criando animais
animal1 = Animal("Mia", "Viralata", "Raiva")
animal2 = Animal("Cagão", "Pastor Alemão","V8")

#criando doações que recebem objetos da classe Animal e Doador
doacao1 = Doacao(1992, 12, 19,animal1, doador1,'Caga muito' )
doacao2 = Doacao(2022, 2, 14,animal2, doador2,'Violento' )

#criando adocões que recebem objetos da classe Animal e Adotante
adocao1 = Adocao(2023,10,15,animal1, adotante1,True)
adocao2 = Adocao(2021,2,28,animal2, adotante2,True)

#criando uma lista de animais, doações e adoções
lista_animais = [animal1,animal2]
lista_doacoes = [doacao1,doacao2]
lista_adocoes = [adocao1,adocao2]

# criando uma instancia de ong e passando  a lista de animais
ong = Ong(lista_animais, lista_doacoes, lista_adocoes)

ong.receber_animal(animal1)
ong.receber_animal(animal2)

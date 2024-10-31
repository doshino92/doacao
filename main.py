from doador import Doador
from animal import Animal
from doacao import Doacao

#adotante1 = Adotante('Gui', '11221643606','Florianópolis',1992,9,19, True, False )

#doacao1 = Doacao(2023,2,12,'Cachorro',doador1,'Pessoal' )
#animal2 = Animal('Cagão', 'Viralata', 'Raiva')

# criando um doador
doador1 = Doador('Rafaela', '11221643606', 'Trindade', 2024, 12, 19,None)

#criando um animal
animal1 = Animal('Mia', 'Viralata', 'Raiva')

#criando uma doação que recebe objetos da classe Animal e Doador
doacao1 = Doacao(1992, 12, 19, animal1,doador1,'Caga muito' )

print(doacao1.doador.nome)

doador1.nome = 'Guilherme'

print(doacao1.doador.nome)
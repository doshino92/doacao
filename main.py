from doador import Doador
from animal import Animal
from doacao import Doacao
from adocao import Adocao
from adotante import Adotante

adotante1 = Adotante('Gui', '11221643606','Florianópolis',1992,9,19, True, False )

#doacao1 = Doacao(2023,2,12,'Cachorro',doador1,'Pessoal' )
#animal2 = Animal('Cagão', 'Viralata', 'Raiva')

# criando um doador
doador1 = Doador('Rafaela', '11221643606', 'Trindade', 2024, 12, 19,None)

#criando um animal
animal1 = Animal('Mia', 'Viralata', 'Raiva')

#criando uma doação que recebe objetos da classe Animal e Doador
doacao1 = Doacao(1992, 12, 19, animal1,doador1,'Caga muito' )

#criando uma adocao que recebe um animal e um adotante
adocao1 = Adocao(2023,10,15,animal1,adotante1,True)

print(adocao1.data_adoacao)
from doador import Doador
from pessoa import Pessoa
from adotante import Adotante
from doador import Doador
from datetime import date
from doacao import Doacao

doador1 = Doador('Rafaela','11221643606','Trindade', 1992,12,19,'Mia')
adotante1 = Adotante('Gui', '11221643606','Florianópolis',1992,9,19, True, False )

doacao1 = Doacao(2023,2,12,'Cachorro',doador1,'Pessoal' )

print(doacao1.doador.nome)
print(doacao1.data_doacao)































from pessoa import Pessoa
from datetime import date


pessoa1 = Pessoa('Gui', '11221643606','Florianópolis',1992,9,19)
print(pessoa1.nome)
pessoa1.nome = "Rodrigo"
print(pessoa1.nome)
print(pessoa1)
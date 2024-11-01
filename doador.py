from animal import Animal
from pessoa import Pessoa


class Doador(Pessoa):
    def __init__(self, nome: str, cpf: str, endereco: str, ano: int, mes: int, dia: int, animal: Animal ):
        super().__init__(nome, cpf, endereco, ano, mes, dia)
        self.__animal =  animal

        @property
        def animal(self):
            return self.__animal

        @animal.setter
        def animal(self, novo_animal: Animal ):
            self.__animal = novo_animal





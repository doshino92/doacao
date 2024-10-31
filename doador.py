from pessoa import Pessoa


class Doador(Pessoa):

    def __init__(self, nome: str, cpf: str, endereco: str, ano: int, mes: int, dia: int, animal_doado: str):
        super().__init__(nome, cpf,endereco,ano, mes, dia)
        self.__animal_doado = animal_doado

    @property
    def animal_doado(self):
        return self.__animal_doado

    @animal_doado.setter
    def animal_doado(self, novo_animal_doado):
        self.__animal_doado = novo_animal_doado





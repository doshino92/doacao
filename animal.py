from vacina import Vacina
from datetime import date
from registroVacina import RegistroVacina

class Animal:
    def __init__(self, nome: str, raca: str, adotado: bool = False):
        self.__nome = nome
        self.__raca = raca
        self.__adotado = adotado

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca: str):
        self.__raca = nova_raca

    @property
    def adotado(self):
        return self.__adotado

    @adotado.setter
    def adotado(self, novo_adotado: bool):
        self.__adotado = novo_adotado

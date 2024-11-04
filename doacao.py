from doador import Doador
from animal import Animal
from datetime import date


class Doacao:
    def __init__(self, ano: int, mes: int, dia: int, animal: Animal, doador: Doador, motivo: str):
        self.__data_doacao = date(ano, mes, dia)
        self.__animal = animal
        self.__doador = doador
        self.__motivo = motivo

        if isinstance(self.data_doacao, date):
            self.__data_doacao = date(ano,mes,dia)

        if isinstance(self.animal, Animal):
            self.__animal = animal

        if isinstance(self.doador, Doador):
            self.__doador = doador

        if isinstance(self.motivo, str):
            self.__motivo = motivo

    @property
    def data_doacao(self):
        return self.__data_doacao

    @data_doacao.setter
    def data_doacao(self, nova_data_doacao):
        if isinstance(nova_data_doacao, Doacao):
            dia, mes, ano = map(int, nova_data_doacao.split('-')) #split coloca traço entre as datas e ajusta para dia, mes ano
            self.__data_doacao = date(ano, mes, dia)              #map(int)  força string a virar um inteiro

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, novo_animal: Animal):
        if isinstance(novo_animal, Animal):
            self.__animal = novo_animal

    @property
    def doador(self):
        return self.__doador

    @doador.setter
    def doador(self, novo_doador: Doador):
         if isinstance(novo_doador, Doador):
            self.__doador = novo_doador

    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, novo_motivo: str):
        if isinstance(novo_motivo, str):
            self.__motivo = novo_motivo







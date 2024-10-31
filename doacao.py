from doador import Doador
from datetime import date
from animal import Animal


class Doacao:
    def __init__(self, ano: int, mes: int, dia: int, animal: str, doador: Doador, motivo: str):
        self.__data_doacao = date(ano, mes, dia)
        self.__animal = animal
        self.__doador = doador
        self.__motivo = motivo

    @property
    def data_doacao(self):
        return self.__data_doacao.strftime('%d/%m/%Y')

    @data_doacao.setter
    def data_doacao(self, nova_data_doacao):
        try:
            dia, mes, ano = map(int, nova_data_doacao.split('-')) #split força o usuario a coloca traço entre as datas e ajusto para dia, mes ano
            self.__data_doacao = date(ano, mes, dia)              #map(int)  força string a virar um inteiro
        except ValueError:
            raise ValueError("A data deve estar entre traços Ex: DD-MM-AAAA")

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, novo_animal: Animal):
        self.__animal = novo_animal

    @property
    def doador(self):
        return self.__doador

    @doador.setter
    def doador(self, novo_doador: Doador):
        self.__doador = novo_doador

    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, novo_motivo: str):
        self.__motivo = novo_motivo







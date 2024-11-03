from datetime import date
from tipoVacina import TipoVacina


class Vacina:
    def __init__(self, tipo: TipoVacina, ano: int, mes: int, dia: int):
        self.__tipo = tipo
        self.__data_aplicacao = date(ano, mes, dia)

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo_tipo: TipoVacina):
        self.__tipo = novo_tipo

    @property
    def data_aplicacao(self):
        return self.__data_aplicacao

    @data_aplicacao.setter
    def data_aplicacao(self, nova_data_aplicacao):
        dia, mes, ano = map(int, nova_data_aplicacao.split('-'))
        self.__data_aplicacao = date(ano, mes, dia)
from datetime import date
from animal import Animal
from adotante import Adotante
from doador import Doador


class Adocao:
    def __init__(self, ano, mes, dia, animal: Animal, adotante: Adotante, doador: Doador,termo: bool):
        self.__data_adocao = date(ano, mes, dia)
        self.__animal = None
        self.__adotante = None
        self.__termo = None
        self.__doador = None

        if isinstance(self.__data_adocao, date):
            self.__data_adocao = date(ano, mes, dia)

        if isinstance(animal, Animal):
            self.__animal = animal

        if isinstance(adotante, Adotante):
            self.__adotante = adotante

        if isinstance(termo, bool):
            self.__termo = termo

        if isinstance(doador, Doador):
            self.__doador = doador

        #if isinstance(self.__animal.adotado, Animal):
        self.__animal.adotado = False # marca no Animal que foi Adotado

    @property
    def data_adocao(self):
        return self.__data_adocao

    @data_adocao.setter
    def data_adocao(self, nova_data_adocao):
        if isinstance(nova_data_adocao, date):
            dia, mes, ano = map(int, nova_data_adocao.split('-'))
            self.__data_adocao = date(ano, mes, dia)

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, novo_animal: Animal):
        if isinstance(novo_animal, Animal):
            self.__animal = novo_animal


    @property
    def adotante(self):
        return self.__adotante

    @adotante.setter
    def adotante(self, novo_adotante: Adotante):
        if isinstance(novo_adotante, Adotante):
            self.__adotante = novo_adotante

    @property
    def termo(self):
        return self.__termo

    @termo.setter
    def termo(self, novo_termo: bool):
         if isinstance(novo_termo, bool):
            self.__termo = novo_termo

    @property
    def doador(self):
        return self.__doador

    @doador.setter
    def doador(self, novo_doador: Doador):
        if isinstance(novo_doador, Doador):
            self.__doador = novo_doador

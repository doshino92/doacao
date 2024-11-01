from datetime import date
from animal import Animal
from adotante import Adotante


class Adocao:
    def __init__(self, ano, mes, dia, animal: Animal, adotante: Adotante, termo: bool ):
        self.__data_adoacao = date(ano, mes, dia)
        self.__animal = animal
        self.__adotante = adotante
        self.__termo = None

    @property
    def data_adoacao(self):
        return self.__data_adoacao.strftime('%d/%m/%Y')

    @data_adoacao.setter
    def data_adoacao(self, nova_data_adoacao):
        try:
            dia, mes, ano = map(int, nova_data_adoacao.split(
                '-'))  # split força o usuario a coloca traço entre as datas e ajusto para dia, mes ano
            self.__data_adoacao = date(ano, mes, dia)  # map(int)  força string a virar um inteiro
        except ValueError:
            raise ValueError("A data deve estar entre traços Ex: DD-MM-AAAA")

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, novo_animal: Animal):
        self.__animal = novo_animal

    @property
    def adotante(self):
        return self.__adotante

    @adotante.setter
    def adotante(self, novo_adotante: Adotante):
        self.__adotante = novo_adotante

    @property
    def termo(self):
        return self.__termo

    @termo.setter
    def termo(self, novo_termo: bool):
        self.__termo = novo_termo
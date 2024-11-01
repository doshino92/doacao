import animal
from adocao import Adocao
from animal import Animal
from doacao import Doacao


class Ong:
    def __init__(self, animais: list[Animal], doacoes: list[Doacao], adocoes: list[Adocao]):
        self.__animais = animais
        self.__doacoes = doacoes
        self.__adocoes = adocoes

    def listar_animais(self):
        for animais in self.__animais:  # Usar __animais diretamente
            print(animais.nome)


    def listar_doacoes(self):
        for doacao in self.__doacoes:
            print(doacao.animal.nome)

    def listar_adocoes(self):
        for adocao in self.__adocoes:
            print(adocao.animal.nome)
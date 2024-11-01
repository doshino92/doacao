import animal
from adocao import Adocao
from animal import Animal
from doacao import Doacao


class Ong:
    def __init__(self, animais: list[Animal], doacoes: list[Doacao], adocoes: list[Adocao]):
        self.__animais = animais
        self.__doacoes = doacoes
        self.__adocoes = adocoes

    #mostrar lista de animais que foram doados
    def mostrar_animais(self):
        for animais in self.__animais:  # Usar __animais diretamente
            print(animais.nome)

    #mostrar lista de animais doados
    def mostrar_doacoes(self):
        for doacao in self.__doacoes:
            print(doacao.animal.nome)

    #mostrar lista de animais adotados
    def mostrar_adocoes(self):
        for adocao in self.__adocoes:
            print(adocao.animal.nome)

    def receber_animal(self, animal: Animal):
        self.__animais.append(animal)
        print(f'animal recebido',animal.nome)


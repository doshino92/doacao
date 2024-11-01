import animal
import doador
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
        print(f'Animal recebido',animal.nome)

    def registrar_doacao(self, doacao: Doacao, animal: Animal):
        self.__doacoes.append(doacao)
        print(f'\nDoação Recebida \nAnimal:', animal.nome,'\nDoador: ', doacao.doador.nome )

    def registrar_adocao(self, adocao: Adocao, animal: Animal):
        self.__adocoes.append(adocao)
        print(f'\nAdoção Recebida \nAnimal:', animal.nome,'\nAdotante: ', adocao.adotante.nome )


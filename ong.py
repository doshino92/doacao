from adocao import Adocao
from animal import Animal
from doacao import Doacao
from datetime import date
from datetime import datetime



class Ong:
    def __init__(self, animais: list[Animal], doacoes: list[Doacao], adocoes: list[Adocao] ):
        self.__animais = animais
        self.__doacoes = doacoes
        self.__adocoes = adocoes

    animais_adotados = []
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

    #def verifica_adotante(self):

    def registrar_doacao(self, doacao: Doacao):
        self.__doacoes.append(doacao)
        print(f'\nDoação Recebida \nAnimal:', doacao.animal.nome,'\nDoador: ', doacao.doador.nome )

    def registrar_adocao(self, adocao: Adocao):
        if adocao.adotante.cpf != adocao.doador.cpf:
            self.__adocoes.append(adocao)
            print(f'\nAdoção Realizada \nAnimal:', adocao.animal.nome, '\nAdotante: ', adocao.adotante.nome)
        else:
            print('\n',adocao.doador.nome, 'é doador, então não pode adotar o Animal', adocao.animal.nome )
            adocao.animal.adotado = False # se animal não foi adotado pelo motivo do adotante ser doador, então animal da doação set False em adotado


    def animais_disponiveis(self):
        print("\nAnimais Disponíveis para Adoção:")
        disponiveis = [animal for animal in self.__animais if not animal.adotado] #se animal nao for adotado entra na lista
        for animal in disponiveis:
            print(animal.nome)
        return disponiveis

    def doacoes_por_periodo(self, data_inicio_str: str, data_fim_str: str):
        data_inicio = datetime.strptime(data_inicio_str, '%d-%m-%Y').date()
        data_fim = datetime.strptime(data_fim_str, '%d-%m-%Y').date()

        doacoes_filtradas = []
        doacoes_exibidas = set()  # Para evitar duplicatas

        for doacao in self.__doacoes:
            if data_inicio <= doacao.data_doacao <= data_fim:
                identificador_doacao = (doacao.animal.nome, doacao.doador.nome, doacao.data_doacao)
                if identificador_doacao not in doacoes_exibidas:
                    doacoes_exibidas.add(identificador_doacao)
                    doacoes_filtradas.append(doacao)

        print("\nDoações no período:", data_inicio_str,'até', data_fim_str,'\n' )
        for doacao in doacoes_filtradas:
            print(f"Animal: {doacao.animal.nome}, Doador: {doacao.doador.nome}, Data: {doacao.data_doacao}")

        return doacoes_filtradas


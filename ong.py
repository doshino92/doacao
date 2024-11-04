from adocao import Adocao
from animal import Animal
from doacao import Doacao
from datetime import datetime


class Ong:
    def __init__(self, animais: list[Animal], doacoes: list[Doacao], adocoes: list[Adocao] ):
        self.__animais = []
        self.__doacoes = []
        self.__adocoes = []

        if isinstance(animais, Animal):
            self.__animais.append(animais)
        
        if isinstance(doacoes, Doacao):
            self.__doacoes.append(Doacao)
        
        if isinstance(adocoes, Adocao):
            self.__adocoes.append(Adocao)

    animais_adotados = []

    #mostrar lista de animais que foram doados
    def mostrar_animais(self):
        if isinstance(self.__animais, list):
            for animais in self.__animais:  # Usar __animais diretamente
                print(animais.nome)

    #mostrar lista de animais doados
    def mostrar_doacoes(self):
        if isinstance(self.__doacoes, list):
            for doacao in self.__doacoes:
                print(doacao.animal.nome)

    #mostrar lista de animais adotados
    def mostrar_adocoes(self):
        if isinstance(self.__adocoes, list):
            for adocao in self.__adocoes:
                print(adocao.animal.nome)


    def registrar_doacao(self, doacao: Doacao):
        self.__doacoes.append(doacao)
        print(f'\nDoação Recebida \nAnimal:', doacao.animal.nome,'\nDoador: ', doacao.doador.nome )

    def registrar_adocao(self, adocao: Adocao):
        if adocao.adotante.cpf != adocao.doador.cpf:
            if adocao.adotante.maior_de_idade():  # Verifica se o adotante é maior de idade
                self.__adocoes.append(adocao)
                print(f'\nAdoção Realizada \nAnimal: {adocao.animal.nome} \nAdotante: {adocao.adotante.nome}')
                adocao.animal.adotado = True
            else:
                print(
                    f'\n{adocao.adotante.nome} não pode adotar o animal {adocao.animal.nome} pois não possui 18 anos completos.')
                adocao.animal.adotado = False
        else:
            print(f'\n{adocao.doador.nome} é doador, então não pode adotar o Animal {adocao.animal.nome}')
            adocao.animal.adotado = False  # Se o animal não foi adotado pelo motivo do adotante ser doador, o animal se mantém não adotado


    def animais_disponiveis(self):
        print("\nAnimais Disponíveis para Adoção:")
        disponiveis = [animal for animal in self.__animais if not animal.adotado ]  # Verifica se o animal não foi adotado
        for animal in disponiveis:
            print(animal.nome)
        return disponiveis

    def adocoes_por_periodo(self, data_inicio_str: str, data_fim_str: str):
        data_inicio = datetime.strptime(data_inicio_str, '%d-%m-%Y').date()
        data_fim = datetime.strptime(data_fim_str, '%d-%m-%Y').date()

        resultado = []
        adocoes_exibidas = set()  # Usar um conjunto para evitar duplicatas

        print("\nADOÇÕES no período:", data_inicio_str, 'até', data_fim_str)

        for adocao in self.__adocoes:
            if adocao.animal.adotado and data_inicio <= adocao.data_adocao <= data_fim:
                # Usar uma tupla como chave para identificar adoções
                chave_adocao = (adocao.animal.nome, adocao.adotante.nome, adocao.data_adocao)
                if chave_adocao not in adocoes_exibidas:
                    adocoes_exibidas.add(chave_adocao)  # Adiciona a chave ao conjunto
                    resultado.append(adocao)

        if resultado:
            for adocao in resultado:
                print(f"Animal: {adocao.animal.nome}, Adotante: {adocao.adotante.nome}, Data: {adocao.data_adocao}")
        else:
            print("Nenhuma adoção ocorreu neste período.")

        return resultado

    def doacoes_por_periodo(self, data_inicio_str: str, data_fim_str: str):
        data_inicio = datetime.strptime(data_inicio_str, '%d-%m-%Y').date()
        data_fim = datetime.strptime(data_fim_str, '%d-%m-%Y').date()

        resultado = []
        doacoes_exibidas = set()  # Usar um conjunto para evitar duplicatas

        print("\nDOAÇÕES no período:", data_inicio_str, 'até', data_fim_str)

        for doacao in self.__doacoes:
            if data_inicio <= doacao.data_doacao <= data_fim:
                # Usar uma tupla como chave para identificar doações
                chave_doacao = (doacao.animal.nome, doacao.doador.nome, doacao.data_doacao)
                if chave_doacao not in doacoes_exibidas:
                    doacoes_exibidas.add(chave_doacao)  # Adiciona a chave ao conjunto
                    resultado.append(doacao)

        if resultado:
            for doacao in resultado:
                print(f"Animal: {doacao.animal.nome}, Doador: {doacao.doador.nome}, Data: {doacao.data_doacao}")
        else:
            print("Nenhuma doação ocorreu neste período.")

        return resultado

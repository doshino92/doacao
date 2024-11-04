from adocao import Adocao
from animal import Animal
from doacao import Doacao
from datetime import datetime


class Ong:
    def __init__(self, animais: list[Animal], doacoes: list[Doacao], adocoes: list[Adocao] ):
        self.__animais = animais
        self.__doacoes = doacoes
        self.__adocoes = adocoes

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
        #print(f'\nDoação Recebida \nAnimal:', doacao.animal.nome,'\nDoador: ', doacao.doador.nome )

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
        adocoes_filtradas = []
        for adocao in self.__adocoes:
            if adocao.animal.adotado and data_inicio <= adocao.data_adocao <= data_fim:
                adocoes_filtradas.append(adocao)
        return adocoes_filtradas
        print("\nADOÇÕES no período:", data_inicio_str, 'até', data_fim_str)
        if adocoes_filtradas:
            for adocao in adocoes_filtradas:
                print(f"Animal: {adocao.animal.nome}, Adotante: {adocao.adotante.nome}, Data: {adocao.data_adocao}")
        else:
            print("Nenhuma adoção ocorreu neste período.")
        return adocoes_filtradas

    def doacoes_por_periodo(self, data_inicio_str: str, data_fim_str: str):
        # Converter strings de data para objetos date
        data_inicio = datetime.strptime(data_inicio_str, '%d-%m-%Y').date()
        data_fim = datetime.strptime(data_fim_str, '%d-%m-%Y').date()
        doacoes_filtradas = []
        for doacao in self.__doacoes:
            if data_inicio <= doacao.data_doacao <= data_fim:
                # Verificar se animal e doador não são None antes de acessar nome
                if doacao.animal and doacao.doador:
                    doacoes_filtradas.append(doacao)
        return doacoes_filtradas
        print("\nDOAÇOES no período:", data_inicio_str, 'até', data_fim_str)
        for doacao in doacoes_filtradas:
            print(f"Animal: {doacao.animal.nome}, Adotante: {doacao.doador.nome}, Data: {doacao.data_doacao}")
        return doacoes_filtradas

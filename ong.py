from adocao import Adocao
from animal import Animal
from doacao import Doacao
from datetime import datetime, date
from vacina import Vacina


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


    def registrar_doacao(self, doacao: Doacao):
        self.__doacoes.append(doacao)
        #print(f'\nDoação Recebida \nAnimal:', doacao.animal.nome,'\nDoador: ', doacao.doador.nome )

    def registrar_adocao(self, adocao: Adocao):
        if adocao.adotante.cpf != adocao.doador.cpf:
            self.__adocoes.append(adocao)
            #print(f'\nAdoção Realizada \nAnimal: {adocao.animal.nome} \nAdotante: {adocao.adotante.nome}')
            adocao.animal.adotado = True
        else:
            print(f'\n{adocao.doador.nome} é doador, então não pode adotar o Animal {adocao.animal.nome}')
            adocao.animal.adotado = False  # Se o animal não foi adotado pelo motivo do adotante ser doador, o animal se mantém não adotado


    def animais_disponiveis(self):
        print("\nAnimais Disponíveis para Adoção:")
        disponiveis = [animal for animal in self.__animais if not animal.adotado ]  # Verifica se o animal tem todas as vacinas e não foi adotado
        for animal in disponiveis:
            print(animal.nome)
        return disponiveis

    def adocoes_por_periodo(self, data_inicio_str: str, data_fim_str: str):
        # Converter strings de data para objetos date
        data_inicio = datetime.strptime(data_inicio_str, '%d-%m-%Y').date()
        data_fim = datetime.strptime(data_fim_str, '%d-%m-%Y').date()

        adocoes_filtradas = []
        adocoes_exibidas = set()  # Para evitar duplicatas

        for adocao in self.__adocoes:
            if data_inicio <= adocao.data_adocao <= data_fim:
                identificador_adocao = (adocao.animal.nome, adocao.adotante.nome, adocao.data_adocao)
                if identificador_adocao not in adocoes_exibidas:
                    adocoes_exibidas.add(identificador_adocao)
                    adocoes_filtradas.append(adocao)

        print("\nADOÇÕES no período:", data_inicio_str, 'até', data_fim_str)
        for adocao in adocoes_filtradas:
            print(f"Animal: {adocao.animal.nome}, Adotante: {adocao.adotante.nome}, Data: {adocao.data_adocao}")

        return adocoes_filtradas

    def doacoes_por_periodo(self, data_inicio_str: str, data_fim_str: str):
        # Converter strings de data para objetos date
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

        print("\nDOAÇOES no período:", data_inicio_str, 'até', data_fim_str)
        for doacao in doacoes_filtradas:
            print(f"Animal: {doacao.animal.nome}, Adotante: {doacao.doador.nome}, Data: {doacao.data_doacao}")

        return doacoes_filtradas

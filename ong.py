from adocao import Adocao
from animal import Animal
from doacao import Doacao
from datetime import datetime
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
        # Converter strings de data para objetos date
        data_inicio = datetime.strptime(data_inicio_str, '%d-%m-%Y').date()
        data_fim = datetime.strptime(data_fim_str, '%d-%m-%Y').date()

        adocoes_filtradas = []
        adocoes_exibidas = set()  # Para evitar duplicatas

        for adocao in self.__adocoes:
            # Verifica se a adoção foi efetiva (animal foi adotado) e se está dentro do período
            if adocao.animal.adotado and data_inicio <= adocao.data_adocao <= data_fim:
                identificador_adocao = (adocao.animal.nome, adocao.adotante.nome, adocao.data_adocao)
                if identificador_adocao not in adocoes_exibidas:
                    adocoes_exibidas.add(identificador_adocao)
                    adocoes_filtradas.append(adocao)

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

    def vacinar_animais_disponiveis(self, vacina: Vacina):
        print("\nVacinação dos Animais Disponíveis:")
        for animal in self.__animais:
            if not animal.adotado:
                animal.adicionar_vacina(vacina)
                print(f"Vacina {vacina.tipo.value} aplicada em {animal.nome}.")

    def mostrar_vacinas_animal(self, animal):
        if not isinstance(animal, Animal):
            print("O objeto fornecido não é um animal.")
            return

        if not animal.vacinas:
            print(f"{animal.nome} não recebeu vacinas.")
            return

        print(f"Vacinas de {animal.nome}:")
        for vacina in animal.vacinas:
            data = vacina.data_aplicacao  # Obtém o objeto date
            print(
                f"- {vacina.tipo.value} (Data: {data.day}/{data.month}/{data.year})")  # Usa o dia, mês e ano do objeto date
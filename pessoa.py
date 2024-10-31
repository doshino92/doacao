from datetime import date


class Pessoa:
    def __init__(self, nome: str, cpf:str, endereco:str, ano, mes, dia):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__data_nascimento = date(ano, mes, dia)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf: str):
        self.__cpf = novo_cpf

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco: str):
        self.__endereco = novo_endereco

    @property
    def data_nascimento(self):
        return self.__data_nascimento.strftime('%d/%m/%Y') #strftime  para data ser dia, mes e ano, ao inves de ano, mes e dia

    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento: str):
        try:
            dia, mes, ano = map(int, nova_data_nascimento.split('-')) #split força o usuario a coloca traço entre as datas e ajusto para dia, mes ano
            self.__data_nascimento = date(ano, mes, dia)              #map(int)  força string a virar um inteiro
        except ValueError:
            raise ValueError("A data deve estar entre traços Ex: DD-MM-AAAA")

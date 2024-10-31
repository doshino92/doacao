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



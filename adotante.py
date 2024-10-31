from pessoa import Pessoa


class Adotante(Pessoa):
    def __init__(self,nome: str, cpf: str, endereco: str, ano: int, mes: int, dia: int, e_doador: bool, mora_apto: bool):
        super().__init__(nome, cpf,endereco,ano, mes, dia)
        self.__e_doador = e_doador
        self.__mora_apto = mora_apto

    @property
    def e_doador(self):
        return self.__e_doador

    @e_doador.setter
    def e_doador(self, novo_e_doador: bool):
        self.__e_doador = novo_e_doador

    @property
    def mora_apto(self):
        return self.__mora_apto

    @mora_apto.setter
    def mora_apto(self,novo_mora_apto: bool):
        self.__mora_apto = novo_mora_apto

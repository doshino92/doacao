from datetime import date
from pessoa import Pessoa
from tipos import TipoMoradia


class Adotante(Pessoa):
    def __init__(self,nome: str, cpf: str, endereco: str, ano: int, mes: int, dia: int, tipo_moradia: TipoMoradia,
                 e_doador: bool= None, mora_apto: bool = None, ja_tem_animal: bool = None):
        super().__init__(nome, cpf,endereco,ano, mes, dia)
        self.__e_doador = None
        self.__mora_apto = None
        self.__ja_tem_animal = None
        self.__tipo_moradia = tipo_moradia

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

    @property
    def ja_tem_animal(self):
        return self.__ja_tem_animal

    @ja_tem_animal.setter
    def ja_tem_animal(self,novo_ja_tem_animal: bool):
        self.__ja_tem_animal = novo_ja_tem_animal

    def maior_de_idade(self):
        ano_atual = date.today().year
        return (ano_atual - self._Pessoa__data_nascimento.year)  >= 18

    @property
    def tipo_moradia(self):
        return self.__tipo_moradia

    @tipo_moradia.setter
    def tipo_moradia(self,nova_tipo_moradia: TipoMoradia):
        self.__tipo_moradia = nova_tipo_moradia



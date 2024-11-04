from datetime import date
from pessoa import Pessoa
from moradia import Moradia


class Adotante(Pessoa):
    def __init__(self,nome: str, cpf: str, endereco: str, ano: int, mes: int, dia: int, tipo_moradia: Moradia,
                 e_doador: bool, ja_tem_animal: bool):
        super().__init__(nome, cpf,endereco,ano, mes, dia)
        self.__e_doador = None
        self.__ja_tem_animal = None
        self.__tipo_moradia = None


        if isinstance(e_doador, bool):
            self.__e_doador = e_doador

        if isinstance(ja_tem_animal, bool):
            self.__ja_tem_animal = ja_tem_animal

        if isinstance(tipo_moradia, Moradia):
            self.__tipo_moradia = tipo_moradia

    @property
    def e_doador(self):
        return self.__e_doador

    @e_doador.setter
    def e_doador(self, novo_e_doador: bool):
        if isinstance(novo_e_doador, str):
            self.__e_doador = novo_e_doador

    @property
    def ja_tem_animal(self):
        return self.__ja_tem_animal

    @ja_tem_animal.setter
    def ja_tem_animal(self,novo_ja_tem_animal: bool):
        if isinstance(novo_ja_tem_animal, str):
            self.__ja_tem_animal = novo_ja_tem_animal

    def maior_de_idade(self):
        ano_atual = date.today().year
        return (ano_atual - self._Pessoa__data_nascimento.year)  >= 18

    @property
    def tipo_moradia(self):
        return self.__tipo_moradia

    @tipo_moradia.setter
    def tipo_moradia(self,nova_tipo_moradia: Moradia):
        if isinstance(nova_tipo_moradia, Moradia):
            self.__tipo_moradia = nova_tipo_moradia



from tipos import TipoPorte
from tipos import TipoAnimal
from vacina import Vacina
from typing import List


class Animal:
    def __init__(self,chip: str, nome: str, raca: str, porte: TipoPorte,
                 tipo_animal: TipoAnimal, adotado: bool = False):
        self.__chip = None
        self.__nome = None
        self.__raca = None
        self.__porte = None
        self.__tipo_animal = None
        self.__adotado = None
        self.__vacinas = []

        if isinstance(chip, str):
            self.__chip = chip

        if isinstance(nome, str):
            self.__nome = nome

        if isinstance(raca, TipoAnimal):
            self.__raca = raca

        if isinstance(adotado, bool):
            self.__adotado = adotado

    @property
    def chip(self):
        return self.__chip

    @chip.setter
    def chip(self, novo_chip: str):
        if isinstance(novo_chip, str):
            self.__chip = novo_chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca: str):
        if isinstance(nova_raca, TipoAnimal):
            self.__raca = nova_raca

    @property
    def porte(self):
        return self.__porte

    @porte.setter
    def porte(self, novo_porte: TipoPorte):
        self.__porte = novo_porte

    @property
    def tipo_animal(self):
        return self.__tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, novo_tipo_animal: TipoAnimal):
        self.__tipo_animal = novo_tipo_animal

    @property
    def vacinas(self) -> List[Vacina]:
        return self.__vacinas

    def adicionar_vacina(self, vacina: Vacina):
        self.__vacinas.append(vacina)

    @property
    def adotado(self):
        return self.__adotado

    @adotado.setter
    def adotado(self, novo_adotado: bool):
        self.__adotado = novo_adotado

    def mostrar_vacinas(self):
        if not self.vacinas:
            print(f"{self.nome} não recebeu vacinas.")
            return
        print(f"Vacinas de {self.nome}:")
        for vacina in self.vacinas:
            print(f"- {vacina.tipo.value} ")

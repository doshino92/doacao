from tipos import TipoPorte
from tipos import TipoAnimal
from vacina import Vacina
from typing import List


class Animal:
    def __init__(self, nome: str, chip: str, cpf_doador: int, raca: str, porte: str, hepatite: bool, leptospirose: bool, raiva: bool):
        self.__nome = None
        self.__chip = None
        self.__cpf_doador = None
        self.__raca = None
        self.__porte = None
        self.__hepatite = None
        self.__leptospirose = None
        self.__raiva = None
    
        if isinstance(nome, str):
            self.__nome = nome

        if isinstance(chip, str):
            self.__chip = chip
        
        if isinstance(cpf_doador, int):
            self.__cpf_doador = cpf_doador

        if isinstance(raca, str):
            if raca == 'cachorro' or raca == 'gato':
                self.__raca = raca
                
        if isinstance(porte, str):
            if raca == 'cachorro':
                self.__porte = porte
        
        if isinstance(hepatite, bool):
            self.__hepatite = hepatite
        
        if isinstance(leptospirose, bool):
            self.__leptospirose = leptospirose
        
        if isinstance(raiva, bool):
            self.__raiva = raiva
        

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
    
    @property
    def chip(self):
        return self.__chip

    @chip.setter
    def chip(self, chip: str):
        if isinstance(chip, str):
            self.__chip = chip

    @property
    def cpf_doador(self):
        return self.__cpf_doador

    @cpf_doador.setter
    def cpf_doador(self, cpf_doador: str):
        if isinstance(cpf_doador, str):
            self.__nome = cpf_doador

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca: str):
        if isinstance(nova_raca, str):
            if nova_raca == 'cachorro' or nova_raca == 'gato':
                self.__raca = nova_raca

    @property
    def porte(self):
        return self.__porte

    @porte.setter
    def porte(self, novo_porte: TipoPorte):
        self.__porte = novo_porte
        
    @property
    def hepatite(self):
        return self.__hepatite
    
    @hepatite.setter
    def hepatite(self, hepatite):
        if isinstance(hepatite, bool):
            self.__hepatite = hepatite
    
    @property
    def leptospirose(self):
        return self.__leptospirose

    @leptospirose.setter
    def leptospirose(self, leptospirose):
        if isinstance(leptospirose, bool):
            self.__leptospirose = leptospirose
    
    @property
    def raiva(self):
        return self.__raiva

    @raiva.setter
    def raiva(self, raiva):
        if isinstance(raiva, bool):
            self.__raiva = raiva

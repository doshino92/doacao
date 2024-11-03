from tela_animal import TelaAnimal
from animal import Animal
from tipos import TipoAnimal
from tipos import TipoPorte
from tipos import TipoVacina

class ControladorAnimal():
    def __init__(self, ong):
        self.__tela_animal = TelaAnimal()
        self.__animal = []
        self.__cachorros = []
        self.__gatos = []
        self.__tela_animal = TelaAnimal
        self.__ong = ong
        
    
    def inclui_animal(self, nome, chip, raca, doador, vacina):
        if raca == 'cachorro':
            porte = input('')
        
    def mostra_animal(self, chip):
        for animal in self.__animal:
            if animal.chip == chip:
                return animal
        return None


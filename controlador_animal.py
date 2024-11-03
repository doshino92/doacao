from tela_animal import TelaAnimal
from animal import Animal


class ControladorAnimal():
    def __init__(self, ong):
        self.__tela_animal = TelaAnimal()
        self.__animal = []
        self.__cachorros = []
        self.__gatos = []
        self.__ong = ong


    def pega_animal_por_chip(self, chip: int):
        for animal in self.__animal:
            if animal.chip == chip:
                return animal
        return None

    def incluir_cachorro(self, nome, chip, cpf_doador, raca, porte, hepatite, leptospirose, raiva):
        if self.pega_animal_por_chip(chip) != None:
            return

        animal = Animal(nome=nome, chip=chip, cpf_doador=cpf_doador, raca=raca, porte=porte, hepatite=hepatite, leptospirose=leptospirose, raiva=raiva)

        self.__animal.append(animal)
        self.__cachorros.append(animal)

    def incluir_gato(self, nome, chip, cpf_doador, raca, hepatite, leptospirose, raiva):
        if self.pega_animal_por_chip(chip) != None:
            return

        animal = Animal(nome=nome, chip=chip, cpf_doador=cpf_doador, raca=raca, hepatite=hepatite, leptospirose=leptospirose, raiva=raiva)

        self.__animal.append(animal)
        self.__cachorros.append(animal)
        
    def mostra_animal(self, animal:Animal):
        if not isinstance(animal, Animal):
            return
        
        dados = {}
        dados['nome'] = animal.nome
        dados['chip'] = animal.chip
        dados['raca'] = animal.raca
        if animal.raca == 'cachorro':
            dados['porte'] = animal.porte
        dados['hepatite'] = animal.hepatite
        dados['leptospirose'] = animal.leptospirose
        dados['raiva'] = animal.raiva
        
        self.__tela_animal.mostrar_animal(dados)
    
    def listar_animal(self, animal:Animal):
        i = 0
        while i < len(self.__animal):
            animal = self.__animal[i]
            self.mostra_animal(animal[i])

            i = i + 1


    def listar_cachorros(self, cachorro:Animal):
        i = 0
        while i < len(self.__cachorros):
            cachorro = self.__cachorros[i]
            self.mostra_animal(cachorro[i])

            i = i + 1
    
    def listar_gatos(self, gato:Animal):
        i = 0
        while i < len(self.__gatos):
            gato = self.__gatos[i]
            self.mostra_animal(gato[i])

            i = i + 1
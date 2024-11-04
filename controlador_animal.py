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

    def incluir_cachorro(self, nome, chip, raca, porte, hepatite, leptospirose, raiva, data_aplicacao_H, data_aplicacao_L, data_aplicacao_R):
        if self.pega_animal_por_chip(chip) != None:
            return

        animal = Animal(nome=nome, chip=chip, raca=raca, porte=porte, hepatite=hepatite, leptospirose=leptospirose, raiva=raiva)

        self.__animal.append(animal)
        self.__cachorros.append(animal)

    def incluir_gato(self, nome, chip, raca, hepatite, leptospirose, raiva, data_aplicacao_H, data_aplicacao_L, data_aplicacao_R):
        if self.pega_animal_por_chip(chip) != None:
            return

        animal = Animal(nome=nome, chip=chip, raca=raca, hepatite=hepatite, leptospirose=leptospirose, raiva=raiva)

        self.__animal.append(animal)
        self.__cachorros.append(animal)
    
    def alterar_animal(self, animal:Animal):
        self.listar_animais()
        
        chip = self.__tela_animal.solicitar_input('chip do animal: ')
        animal = self.pega_animal_por_chip(chip)
        continua = animal != None
        
        if continua:
            if animal.raca == 'cachorro':
                novos_dados_animal = self.__tela_animal.dados_cachorro()
                animal.nome = novos_dados_animal['nome']
                animal.chip = novos_dados_animal['chip']
                animal.raca = 'cachorro'
                animal.porte = novos_dados_animal['porte']
                animal.hepatite = novos_dados_animal['hepatite']
                animal.leptospirose = novos_dados_animal['leptospirose']
                animal.raiva = novos_dados_animal['raiva']
                animal.data_aplicacao_H = novos_dados_animal['data_aplicacao_Hepatite']
                animal.data_aplicacao_L = novos_dados_animal['data_aplicacao_Leptospirose']
                animal.data_aplicacao_R = novos_dados_animal['data_aplicacao_Raiva']

            else:
                novos_dados_animal = self.__tela_animal.dados_gato()
                animal.nome = novos_dados_animal['nome']
                animal.chip = novos_dados_animal['chip']
                animal.raca = 'gato'
                animal.hepatite = novos_dados_animal['hepatite']
                animal.leptospirose = novos_dados_animal['leptospirose']
                animal.raiva = novos_dados_animal['raiva']
                animal.data_aplicacao_H = novos_dados_animal['data_aplicacao_Hepatite']
                animal.data_aplicacao_L = novos_dados_animal['data_aplicacao_Leptospirose']
                animal.data_aplicacao_R = novos_dados_animal['data_aplicacao_Raiva']

        return
        
    def excluir_animal(self, animal:Animal, chip):
        animal = self.pega_animal_por_chip(chip)
        if animal != None:
            if animal.raca == 'cachorro':
                self.__cachorros.remove(animal)
            else:
                if animal.raca == 'cachorro':
                    self.__gatos.remove(animal)

            self.__gatos.remove(animal)        
        return None  

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
    
    def listar_animais(self, animal:Animal):
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

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cachorro, 2: self.incluir_gato, 3: self.alterar_animal, 4: self.excluir_animal, 5: self.mostra_animal, 6: self.listar_animais, 7: self.listar_cachorros, 8: self.listar_gatos}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_animal.tela_inicial()]()

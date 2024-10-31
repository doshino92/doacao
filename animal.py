class Animal:
    def __init__(self, nome: str, raca: str, vacina: str ):
        self.__nome = None
        self.__raca = None
        self.__vacina = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca: str):
        self.__raca = nova_raca

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, nova_vacina: str):
        self.__vacina = nova_vacina

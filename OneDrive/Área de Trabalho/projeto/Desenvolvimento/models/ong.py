# models/ong.py
class Ong:
    def __init__(self):
        self.doadores = []

    def adicionar_doador(self, doador):
        self.doadores.append(doador)

    def listar_doadores(self):
        return self.doadores

    def alterar_doador(self, cpf, nome=None, endereco=None):
        for doador in self.doadores:
            if doador.cpf == cpf:
                if nome:
                    doador.nome = nome
                if endereco:
                    doador.endereco = endereco

    def excluir_doador(self, doador):
        self.doadores.remove(doador)

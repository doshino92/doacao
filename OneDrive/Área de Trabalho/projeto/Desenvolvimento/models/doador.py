# models/doador.py
class Doador:
    def __init__(self, nome, cpf, endereco, ano, mes, dia, animal_doado=None):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = f"{ano}-{mes:02d}-{dia:02d}"
        self.animal_doado = animal_doado

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Endereço: {self.endereco}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Animal Doado: {self.animal_doado}")

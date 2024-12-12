# models/doador.py
class Doador:
    def __init__(self, nome, cpf, endereco, ano, mes, dia):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.ano = ano
        self.mes = mes
        self.dia = dia

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf} - Endereço: {self.endereco} - Nascimento: {self.dia}/{self.mes}/{self.ano}"

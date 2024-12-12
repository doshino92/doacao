from datetime import date

class Doador:
    def __init__(self, nome, cpf, endereco, ano, mes, dia):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nascimento = date(ano, mes, dia) if isinstance(ano, int) else date.fromisoformat(ano)

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Endereço: {self.endereco}\n"
                f"Data de Nascimento: {self.data_nascimento.strftime('%Y-%m-%d')}\n")

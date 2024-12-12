# exceptions/exceptions.py
class CampoObrigatorioVazio(Exception):
    def __init__(self, campo):
        self.campo = campo
        super().__init__(f"O campo {campo} é obrigatório e não pode estar vazio.")

class CPFInvalido(Exception):
    def __init__(self, cpf):
        self.cpf = cpf
        super().__init__(f"O CPF {cpf} é inválido.")

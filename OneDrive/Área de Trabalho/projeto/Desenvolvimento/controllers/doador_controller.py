import pickle
from models.doador import Doador
from datetime import date

class DoadorController:
    def __init__(self):
        self.file_path = 'data/doadores_data.pkl'
        self.doadores = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'rb') as file:
                doadores = pickle.load(file)
                # Converter datas de nascimento que estão no formato string
                for doador in doadores:
                    if isinstance(doador.data_nascimento, str):
                        doador.data_nascimento = date.fromisoformat(doador.data_nascimento)
                return doadores
        except (FileNotFoundError, EOFError):
            return []

    def save_data(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.doadores, file)

    def add_doador(self, doador: Doador):
        if not self.is_valid_cpf(doador.cpf):
            return f'CPF {doador.cpf} é inválido.'
        if not any(d.cpf == doador.cpf for d in self.doadores):
            self.doadores.append(doador)
            self.save_data()
            return f'Doador {doador.nome} adicionado com sucesso.'
        else:
            return f'Doador com CPF {doador.cpf} já existe.'

    def remove_doador(self, cpf: str):
        # Remover a validação de CPF para permitir a exclusão de qualquer CPF
        self.doadores = [doador for doador in self.doadores if doador.cpf != cpf]
        self.save_data()
        return f'Doador com CPF {cpf} removido com sucesso.'

    def update_doador(self, cpf: str, nome: str = None, endereco: str = None, novo_cpf: str = None):
        if not self.is_valid_cpf(cpf):
            return f'CPF {cpf} é inválido.'
        for doador in self.doadores:
            if doador.cpf == cpf:
                if nome:
                    doador.nome = nome
                if endereco:
                    doador.endereco = endereco
                if novo_cpf:
                    if not self.is_valid_cpf(novo_cpf):
                        return f'Novo CPF {novo_cpf} é inválido.'
                    doador.cpf = novo_cpf
                self.save_data()
                return f'Doador com CPF {cpf} atualizado com sucesso.'
        return f'Doador com CPF {cpf} não encontrado.'

    def get_doador(self, cpf: str):
        if not self.is_valid_cpf(cpf):
            return f'CPF {cpf} é inválido.'
        for doador in self.doadores:
            if doador.cpf == cpf:
                return doador
        return None

    def list_doadores(self):
        return self.doadores

    def generate_report(self):
        return '\n'.join(str(d) for d in self.doadores)

    def is_valid_cpf(self, cpf: str):
        return len(cpf) == 11 and cpf.isdigit() and not cpf == cpf[0] * 11

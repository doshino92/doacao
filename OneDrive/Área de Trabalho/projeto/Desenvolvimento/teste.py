# views/tela_geral_view.py
import PySimpleGUI as sg
from models.doador import Doador
from controllers.doador_controller import DoadorController
from exceptions import CampoObrigatorioVazio, CPFInvalido
from utils import validar_cpf

class TelaGeralView:
    def __init__(self):
        self.doador_controller = DoadorController()
        self.menu_doadores()

    def menu_doadores(self):
        layout = [
            [sg.Button('Adicionar Doador')],
            [sg.Button('Listar Doadores')],
            [sg.Button('Alterar Doador')],
            [sg.Button('Excluir Doador')],
            [sg.Button('Gerar Relatório')],
            [sg.Button('Sair')]
        ]
        window = sg.Window('Menu Doadores', layout, size=(400, 300))

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair':
                break
            elif event == 'Adicionar Doador':
                self.adicionar_doador()
            elif event == 'Listar Doadores':
                self.listar_doadores()
            elif event == 'Alterar Doador':
                self.alterar_doador()
            elif event == 'Excluir Doador':
                self.excluir_doador()
            elif event == 'Gerar Relatório':
                self.gerar_relatorio()

        window.close()

    def adicionar_doador(self):
        layout = [
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('CPF:'), sg.InputText(key='cpf')],
            [sg.Text('Endereço:'), sg.InputText(key='endereco')],
            [sg.Text('Ano de Nascimento (YYYY):'), sg.InputText(key='ano')],
            [sg.Text('Mês de Nascimento (1-12):'), sg.InputText(key='mes')],
            [sg.Text('Dia de Nascimento (1-31):'), sg.InputText(key='dia')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Adicionar Doador', layout, size=(400, 300))

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break
            elif event == 'Salvar':
                try:
                    nome = values['nome']
                    cpf = values['cpf']
                    endereco = values['endereco']
                    ano = values['ano']
                    mes = values['mes']
                    dia = values['dia']

                    if any(field == '' for field in [nome, cpf, endereco, ano, mes, dia]):
                        raise CampoObrigatorioVazio('todos')

                    if not validar_cpf(cpf):
                        raise CPFInvalido(cpf)

                    ano = int(ano)
                    mes = int(mes)
                    dia = int(dia)

                    if ano < 0:
                        raise ValueError("Ano inválido! Por favor, insira um ano positivo.")
                    if not (1 <= mes <= 12):
                        raise ValueError("Mês inválido! Por favor, insira um mês entre 1 e 12.")
                    if not (1 <= dia <= 31):
                        raise ValueError("Dia inválido! Por favor, insira um dia entre 1 e 31.")

                    doador = Doador(
                        nome=nome,
                        cpf=cpf,
                        endereco=endereco,
                        ano=ano,
                        mes=mes,
                        dia=dia
                    )
                    feedback = self.doador_controller.add_doador(doador)
                    sg.popup(feedback)
                    if "sucesso" in feedback:
                        break
                except (CampoObrigatorioVazio, CPFInvalido, ValueError) as e:
                    sg.popup(str(e))

        window.close()

    def listar_doadores(self):
        doadores = self.doador_controller.list_doadores()
        layout = [
            [sg.Text('Doadores Cadastrados:')],
            [sg.Multiline(default_text='\n'.join(
                [str(d) for d in doadores]), size=(60, 20))]
        ]
        window = sg.Window('Listar Doadores', layout, size=(400, 300))
        window.read()
        window.close()

    def alterar_doador(self):
        layout = [
            [sg.Text('CPF do Doador a ser alterado:'), sg.InputText(key='cpf')],
            [sg.Text('Novo Nome (deixe vazio para não alterar):'), sg.InputText(key='nome')],
            [sg.Text('Novo Endereço (deixe vazio para não alterar):'), sg.InputText(key='endereco')],
            [sg.Button('Salvar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Alterar Doador', layout, size=(400, 300))

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break
            elif event == 'Salvar':
                try:
                    if values['cpf'] == '':
                        raise CampoObrigatorioVazio('CPF')
                    feedback = self.doador_controller.update_doador(
                        cpf=values['cpf'],
                        nome=values['nome'] if values['nome'] else None,

# app.py
from views.tela_geral_view import TelaGeralView
# views/tela_geral_view.py
from exceptions import CampoObrigatorioVazio, CPFInvalido
# views/tela_geral_view.py
from utils import validar_cpf
# views/tela_geral_view.py
from logs import registrar_alteracao, listar_alteracoes



if __name__ == '__main__':
    TelaGeralView()

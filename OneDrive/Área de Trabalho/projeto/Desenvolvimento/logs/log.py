import pickle
import os
from datetime import datetime

LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, 'alteracoes_log.pkl')
TXT_LOG_FILE = os.path.join(LOG_DIR, 'alteracoes_log.txt')


def registrar_alteracao(cpf, campo, valor_antigo, valor_novo):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    try:
        with open(LOG_FILE, 'rb') as f:
            registros = pickle.load(f)
    except FileNotFoundError:
        registros = []

    novo_registro = {
        'cpf': cpf,
        'campo': campo,
        'valor_antigo': valor_antigo,
        'valor_novo': valor_novo,
        'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    registros.append(novo_registro)

    with open(LOG_FILE, 'wb') as f:
        pickle.dump(registros, f)

    with open(TXT_LOG_FILE, 'a') as f:
        f.write(
            f"{novo_registro['data']} - CPF: {novo_registro['cpf']} - Campo: {novo_registro['campo']} - Antigo: {novo_registro['valor_antigo']} - Novo: {novo_registro['valor_novo']}\n")


def listar_alteracoes():
    try:
        with open(LOG_FILE, 'rb') as f:
            registros = pickle.load(f)
    except FileNotFoundError:
        registros = []

    return registros

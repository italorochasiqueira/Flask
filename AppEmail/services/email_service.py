import json
import os

caminho_json = os.path.join(os.path.dirname(__file__), '..', 'data', 'modelo_email.json')

def carregar_modelo_email():
    '''Carrega o modelo de e-mail do arquivo JSON.'''
    if not os.path.exists(caminho_json):
        return {}
    with open(caminho_json, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_modelo_email(modelo_email):
    '''Salva o modelo de e-mail no JSON.'''
    # Validação
    if not modelo_email.get("conteudo_email"):
        return False, "O campo 'conteudo_email' é obrigatório."

    # Salva diretamente
    with open(caminho_json, 'w', encoding='utf-8') as arquivo:
        json.dump(modelo_email, arquivo, ensure_ascii=False, indent=4)

    return True, "Modelo de e-mail salvo com sucesso."


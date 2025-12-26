import json
import os

caminho_json = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.json')

def carregar_cadastro():
    '''Função para carregar os cadastros do arquivo JSON.'''
    if not os.path.exists(caminho_json):
        return []
    with open(caminho_json, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_cadastro(cadastro):
    '''Função para salvar um novo cadastro no arquivo JSON.'''

    campos_obrigatorios = ['cdc', 'descricao', 'nome', 'email' ]
    for campo in campos_obrigatorios:
        if not cadastro.get(campo):
            return False, f"O campo '{campo}' é obrigatório."
        
    cadastros = carregar_cadastro()
    cadastros.append(cadastro)

    with open(caminho_json, 'w', encoding='utf-8') as arquivo:
        json.dump(cadastros, arquivo, ensure_ascii=False, indent=4)
    
    return True, "Cadastro salvo com sucesso."

def excluir_cadastro_service(cdc):
    '''Função para excluir um cadastro pelo CDC.'''
    
    if not cdc or not str(cdc).strip():
        return False, "CDC inválido."
    
    cadastros = carregar_cadastro()
    cadastros_atualizados = [cadastro for cadastro in cadastros if cadastro.get('cdc') != cdc]

    if len(cadastros) == len(cadastros_atualizados):
        return False, "Cadastro não econtrado"   # Nenhum cadastro foi removido

    with open(caminho_json, 'w', encoding='utf-8') as arquivo:
        json.dump(cadastros_atualizados, arquivo, ensure_ascii=False, indent=4)
    
    return True, "Cadastro excluído com sucesso."
import json
import os
import uuid

caminho_json = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.json')

def carregar_cadastro():
    '''Função para carregar os cadastros do arquivo JSON.'''
    if not os.path.exists(caminho_json):
        return []
    with open(caminho_json, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_cadastro(cadastro):
    '''Função para atualizar ou salvar um novo cadastro no arquivo JSON.'''

    cadastros = carregar_cadastro()

    if cadastro.get("id"):
        # 🔁 Atualização
        atualizado = False
        for item in cadastros:
            if item["id"] == cadastro["id"]:
                item.update({
                    "cdc": cadastro.get("cdc"),
                    "descricao": cadastro.get("descricao"),
                    "nome": cadastro.get("nome"),
                    "email": cadastro.get("email")
                })
                atualizado = True
                break
        if not atualizado:
            return False, "Cadastro não encontrado."
    else:
        # 🆕 Novo cadastro
        campos_obrigatorios = ['cdc', 'descricao', 'nome', 'email']
        for campo in campos_obrigatorios:
            if not cadastro.get(campo):
                return False, f"O campo '{campo}' é obrigatório."

        if any(c.get('cdc') == cadastro['cdc'] for c in cadastros):
            return False, "Já existe um cadastro com este CDC."

        cadastro['id'] = str(uuid.uuid4())
        cadastros.append(cadastro)

    # Salvar no JSON
    with open(caminho_json, 'w', encoding='utf-8') as arquivo:
        json.dump(cadastros, arquivo, ensure_ascii=False, indent=4)

    return True, "Cadastro salvo com sucesso." if not cadastro.get("id") else "Cadastro atualizado com sucesso."

def excluir_cadastro_service(id):
    '''Função para excluir um cadastro pelo ID.'''
    
    if not id or not str(id).strip():
        return False, "ID inválido."
    
    cadastros = carregar_cadastro()
    cadastros_atualizados = [cadastro for cadastro in cadastros if cadastro.get('id') != id]

    if len(cadastros) == len(cadastros_atualizados):
        return False, "Cadastro não econtrado"   # Nenhum cadastro foi removido

    with open(caminho_json, 'w', encoding='utf-8') as arquivo:
        json.dump(cadastros_atualizados, arquivo, ensure_ascii=False, indent=4)
    
    return True, "Cadastro excluído com sucesso."
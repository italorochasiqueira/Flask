import os
import re
from services.cadastro_service import carregar_cadastro
from services.email_service import carregar_modelo_email

def extrair_cdc_nome_arquivo(nome_arquivo):
    """Extrai o CDC do nome do arquivo."""

    if not nome_arquivo:
        return None

    # Remove a extensão
    nome_sem_extensao = os.path.splitext(nome_arquivo)[0].strip()

    # Tenta encontrar um bloco inicial de letras (CDC)
    match = re.match(r'^([A-Za-z]{2,10})', nome_sem_extensao)

    if not match:
        print(f"[WARN] Não foi possível extrair CDC de: {nome_arquivo}")
        return None

    cdc = match.group(1).upper()
    print(f"[INFO] CDC extraído: {cdc}")

    return cdc

def buscar_cadastro_por_cdc(cdc):
    '''Busca o cadastro pelo CDC.'''
    cadastros = carregar_cadastro()

    for cadastro in cadastros:
        if cadastro.get("cdc") == cdc:
            return cadastro

    return None

def processar_importacao(caminho_arquivos):
    """
    Varre uma pasta de rede e prepara os dados para envio de e-mail
    """

    resultados = {
        "processados": [],
        "ignorados": [],
        "erros": []
    }

    modelo_email = carregar_modelo_email()

    for nome_arquivo in os.listdir(caminho_arquivos):
        caminho_arquivo = os.path.join(caminho_arquivos, nome_arquivo)

        if not os.path.isfile(caminho_arquivo):
            continue

        if not nome_arquivo.lower().endswith(".pdf"):
            resultados["ignorados"].append({
                "arquivo": nome_arquivo,
                "motivo": "Não é PDF"
            })
            continue

        cdc = extrair_cdc_nome_arquivo(nome_arquivo)

        if not cdc:
            resultados["erros"].append({
                "arquivo": nome_arquivo,
                "motivo": "CDC não encontrado no nome do arquivo"
            })
            continue

        cadastro = buscar_cadastro_por_cdc(cdc)

        if not cadastro:
            resultados["erros"].append({
                "arquivo": nome_arquivo,
                "motivo": f"CDC {cdc} não cadastrado"
            })
            continue

        resultados["processados"].append({
            "arquivo": nome_arquivo,
            "caminho": caminho_arquivo, 
            "cdc": cdc,
            "destinatario": cadastro["email"],
            "nome": cadastro["nome"],
            "assunto": "Envio automático de documento",
            "corpo": modelo_email.get("conteudo_email", "")
        })

    return resultados
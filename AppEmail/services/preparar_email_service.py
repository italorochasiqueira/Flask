from services.importacao_service import processar_importacao

REMETENTE_PADRAO = "cpf@postalis.org.br"
ASSUNTO_PADRAO = "[CPF] Resultado Orçamentário"

def preparar_email(resultado_importacao):
    """
    Recebe o resultado da importação
    Retorna uma lista de e-mails prontos para envio
    """

    emails = []

    # ==========================
    # Arquivos processados
    # ==========================

    for item in resultado_importacao.get("processados", []):
        emails.append({
            "to": item["destinatario"],
            "from": REMETENTE_PADRAO,
            "subject": ASSUNTO_PADRAO,
            "body": item["conteudo_email"],
            "arquivo": item["arquivo"]
            })

    return emails
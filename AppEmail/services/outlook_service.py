import os
import win32com.client

def enviar_emails_outlook(emails, pasta_anexos=None, enviar=False):
    """
    Cria e-mails no Outlook.

    :param emails: lista de dicionários com:
        - to
        - from
        - subject
        - body
        - arquivo (nome do arquivo)
    :param pasta_anexos: caminho onde estão os arquivos
    :param enviar: False = deixa na Caixa de Saída | True = envia direto
    """

    outlook = win32com.client.Dispatch("Outlook.Application")

    enviados = []

    for email in emails:
        try:
            mail = outlook.CreateItem(0)  # 0 = MailItem

            mail.To = email["to"]
            mail.Subject = email["subject"]
            mail.Body = email["body"]

            # Outlook normalmente ignora o "From" se não for conta válida
            # Mas deixamos preparado
            # mail.SentOnBehalfOfName = email["from"]

            # =====================
            # Anexo
            # =====================
            if email.get("arquivo") and pasta_anexos:
                caminho_arquivo = os.path.join(pasta_anexos, email["arquivo"])

                if os.path.exists(caminho_arquivo):
                    mail.Attachments.Add(caminho_arquivo)
                else:
                    raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

            # =====================
            # Enviar ou salvar
            # =====================
            if enviar:
                mail.Send()
            else:
                mail.Save()  # salva como rascunho

            enviados.append(email["to"])

        except Exception as e:
            print(f"Erro ao processar e-mail para {email['to']}: {e}")

    return {
        "enviados": enviados,
    }

from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.email_service import carregar_modelo_email, salvar_modelo_email

email_bp = Blueprint("email", __name__, template_folder="../templates")

@email_bp.route("/email", methods=["GET", "POST"])
def email_page():
    '''implementa a rota para a página de modelo de e-mail.'''
    if request.method == "POST":
        conteudo = request.form.get("conteudo_email", "")
        sucesso, mensagem = salvar_modelo_email({"conteudo_email": conteudo})
        flash(mensagem, "success" if sucesso else "error")
        return redirect(url_for("email.email_page"))

    modelo = carregar_modelo_email()
    return render_template(
        "pag_email.html",
        conteudo_email=modelo.get("conteudo_email", "")
    )

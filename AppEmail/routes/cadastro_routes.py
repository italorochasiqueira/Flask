from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify
from services.cadastro_service import carregar_cadastro, salvar_cadastro

cadastro_bp = Blueprint("cadastrar", __name__)

## Rota para página de cadastro
@cadastro_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        cadastro = {
            "id": request.form.get("id"),
            "cdc": request.form.get("cdc"),
            "descricao": request.form.get("descricao"),
            "nome": request.form.get("nome"),
            "email": request.form.get("email")
        }

        sucesso, mensagem = salvar_cadastro(cadastro)
        if sucesso:
            flash(mensagem, "success")
        else:
            flash(mensagem, "error")
        
        return redirect(url_for("cadastrar.cadastrar"))

    cadastros = carregar_cadastro()
    return render_template("pag_cadastrar.html", cadastros=cadastros)


## Rota para exclusão de cadastro
@cadastro_bp.route("/cadastro/excluir/<id>", methods=["DELETE"])
def excluir_cadastro(id):
    from services.cadastro_service import excluir_cadastro_service

    print(f"Rota de exclusão acessada para ID: {id}")
    sucesso, mensagem = excluir_cadastro_service(id)
    return {"success": sucesso, "message": mensagem}


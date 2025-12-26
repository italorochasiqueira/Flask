from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify
from services.cadastro_service import carregar_cadastro, salvar_cadastro

cadastro_bp = Blueprint("cadastrar", __name__)

@cadastro_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        cadastro = {
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

@cadastro_bp.route("/cadastro/excluir/<cdc>", methods=["DELETE"])
def excluir_cadastro(cdc):
    from services.cadastro_service import excluir_cadastro_service
    
    print(f"Rota de exclusão acessada para CDC: {cdc}")
    sucesso, mensagem = excluir_cadastro_service(cdc)
    return {"success": sucesso, "message": mensagem}

@cadastro_bp.route("/importar_arquivos", methods=["GET"])
def importar_arquivos():
    print("Rota de importação de arquivos acessada.")
    return render_template("pag_import_files.html")
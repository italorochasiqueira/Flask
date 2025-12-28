import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.importacao_service import processar_importacao

importar_bp = Blueprint("importar", __name__, template_folder="../templates")

## Rota para página de importação de arquivos
@importar_bp.route("/importar", methods=["GET", "POST"])
def importar_arquivos():
    if request.method == "POST":
        arquivos = request.files.getlist("file_input")

        if not arquivos:
            flash("Nenhum arquivo selecionado.", "error")
            return redirect(url_for("importar.importar_arquivos"))

        resultados = processar_importacao(arquivos)

        # DEBUG (importante nessa fase)
        print("[DEBUG] Resultado da importação:")
        print(resultados)

        return render_template(
            "pag_import_files.html",
            resultados=resultados
        )

    # ===== GET =====
    print("[INFO] Rota de importação de arquivos acessada.")
    return render_template(
            "pag_import_files.html",
            resultados=None
        )


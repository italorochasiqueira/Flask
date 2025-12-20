from flask import Blueprint, render_template

cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro")
def view():
    return render_template("pag_cadastrar.html")
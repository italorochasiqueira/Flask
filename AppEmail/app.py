import os
from flask import Flask, render_template
from routes.cadastro_routes import cadastro_bp
from routes.email_routes import email_bp
from routes.importar_routes import importar_bp

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "fallback-dev")
app.register_blueprint(cadastro_bp)
app.register_blueprint(email_bp)
app.register_blueprint(importar_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    

import os
from flask import Flask, render_template
from routes.main_routes import cadastro_bp

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "fallback-dev")
app.register_blueprint(cadastro_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    

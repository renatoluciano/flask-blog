from flask import Flask

# Inicializa a aplicação Flask
app = Flask(__name__)

# Cria a página inicial do blog
@app.route("/")
def home():
    return "<h1>Bem-vindo ao nosso Blog!</h1>"

# Roda o servidor se executarmos este arquivo diretamente
if __name__ == "__main__":
    app.run(debug=True)

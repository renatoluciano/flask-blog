from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configura o banco de dados SQLite de forma correta (salvo na pasta 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão do SQLAlchemy passando o nosso app Flask
db = SQLAlchemy(app)

# --- Modelo do Banco de Dados ---
# Define como será a tabela 'post' dentro do nosso banco de dados
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.titulo}>'

# --- Rotas ---
# Rota da página inicial do blog
@app.route("/")
def home():
    # Busca todos os posts salvos na tabela do banco de dados
    posts = Post.query.all()
    # Envia a lista de posts para o template HTML
    return render_template("index.html", posts=posts)


# Roda o servidor local se executarmos este arquivo diretamente
if __name__ == "__main__":
    app.run(debug=True)

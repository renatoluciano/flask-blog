from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configura o banco de dados SQLite (salvo na pasta 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão do SQLAlchemy passando o nosso app Flask
db = SQLAlchemy(app)

# --- Modelo do Banco de Dados ---
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.titulo}>'

# --- Rotas ---

# 1. Rota da página inicial (Lista todos os posts)
@app.route("/")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

# 2. Rota para criar um novo post
@app.route("/post/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        titulo_formulario = request.form["titulo"]
        conteudo_formulario = request.form["conteudo"]
        
        novo_post = Post(titulo=titulo_formulario, conteudo=conteudo_formulario)
        db.session.add(novo_post)
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template("create_post.html")

# 3. Rota para EDITAR um post existente
@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if request.method == "POST":
        post.titulo = request.form["titulo"]
        post.conteudo = request.form["conteudo"]
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template("edit_post.html", post=post)

# 4. Rota para EXCLUIR um post existente
@app.route("/post/<int:post_id>/delete")
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("home"))

# Roda o servidor local
if __name__ == "__main__":
    app.run(debug=True)

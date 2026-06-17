from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configurações do Banco de Dados SQLite (salvo na pasta 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Chave secreta necessária para gerenciar as sessões de login com segurança
app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura-aqui'

# Inicializa a extensão do SQLAlchemy
db = SQLAlchemy(app)

# Configura o gerenciador de login do Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Redireciona para cá se a página exigir login

# --- Modelos do Banco de Dados ---

# Tabela de Posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.titulo}>'

# Tabela de Usuários
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Função obrigatória para o Flask-Login carregar o usuário da sessão
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --- Rotas do Blog ---

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

# 3. Rota para editar um post existente
@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if request.method == "POST":
        post.titulo = request.form["titulo"]
        post.conteudo = request.form["conteudo"]
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template("edit_post.html", post=post)

# 4. Rota para excluir um post existente
@app.route("/post/<int:post_id>/delete")
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("home"))

# 5. Rota para cadastro de novos usuários
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        
        senha_criptografada = generate_password_hash(password)
        
        novo_usuario = User(username=username, email=email, senha_hash=senha_criptografada)
        db.session.add(novo_usuario)
        db.session.commit()
        
        return redirect(url_for("login"))
        
    return render_template("register.html")

# 6. Rota para login de usuários
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.senha_hash, password):
            login_user(user)
            return redirect(url_for("home"))
            
        return redirect(url_for("login"))
        
    return render_template("login.html")

# 7. Rota para logout de usuários
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


# Executa o servidor local
if __name__ == "__main__":
    app.run(debug=True)

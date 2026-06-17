# Flask Blog

Blog modular em Flask estruturado com Git e venv. Usa SQLAlchemy para banco de dados, Flask-WTF em formulários e Flask-Login para controle de usuários. Possui templates HTML dinâmicos e senhas com hash Werkzeug, unindo segurança e desempenho em uma arquitetura limpa e escalável para publicação e gerenciamento de posts na web.

## 🚀 Funcionalidades

* **Autenticação Completa**: Cadastro de usuários com criptografia de senha (`Werkzeug`) e gerenciamento de sessões de login/logout (`Flask-Login`).
* **CRUD de Posts**: Criação, listagem, edição e exclusão de postagens armazenadas em banco de dados.
* **Rotas Protegidas**: Restrição de segurança que impede usuários não autenticados de criar, editar ou remover posts.
* **Interface Responsiva**: Layout minimalista desenvolvido com HTML5 estruturado por herança de templates (`Jinja2`) e estilizado com CSS3 personalizado.

## 📁 Estrutura do Projeto

```text
flask-blog/
├── instance/               # Pasta gerada automaticamente (Banco de Dados SQLite)
│   └── blog.db
├── static/                 # Arquivos estáticos do sistema
│   └── css/
│       └── style.css
├── templates/              # Páginas visuais do sistema (HTML + Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── create_post.html
│   ├── edit_post.html
│   ├── login.html
│   └── register.html
├── venv/                   # Ambiente virtual Python (Ignorado no Git)
├── .gitignore              # Filtro de arquivos protegidos do repositório
└── app.py                  # Arquivo principal do servidor Flask
```

## 🛠️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3.10+](https://python.org)
* [Git](https://git-scm.com)

## 🔧 Instalação e Execução

Siga os passos abaixo para clonar e rodar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd flask-blog
   ```

2. **Crie e ative o ambiente virtual (`venv`):**
   * **Windows:**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências do projeto:**
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Login
   ```

4. **Inicialize as tabelas do Banco de Dados:**
   Abra o interpretador interativo do Python no terminal:
   ```bash
   python
   ```
   Dentro do prompt do Python (`>>>`), execute os comandos para gerar o arquivo do banco de dados:
   ```python
   from app import app, db
   with app.app_context():
       db.create_all()
   exit()
   ```

5. **Rode a aplicação:**
   ```bash
   python app.py
   ```
   Abra o seu navegador e acesse: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido por [Renato Luciano](https://github.com) 👋

from flask import Flask, request, render_template_string

app = Flask(__name__)

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    
    usuarios = [
        {'usuario': 'dolga', 'senha': 'cotemig2026'},
        {'usuario': 'janaina', 'senha': 'cotemig2026'},
        {'usuario': 'antonio', 'senha': 'cotemig2026'},
    ]

    for usuario in usuarios:
        if usuario == i and senha == usuarios[i]:
            return f"<h1>Bem-vindo, {usuario}!</h1>"
    
    if usuario == 'admin' and senha == '123':
        return f"<h1>Bem-vindo, {usuario}!</h1>"
    else:
        return "<h1>Login inválido</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)

# site de consulta https://flask.palletsprojects.com/en/stable/quickstart/#html-escaping
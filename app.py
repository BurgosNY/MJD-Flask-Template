from flask import Flask, render_template
app = Flask(__name__) # Cria uma instância do Flask. 


# Define rota da página principal
@app.route('/')
def index():
    return render_template('index.html') # Renderiza o template index.html, localizado na pasta templates


if __name__ == '__main__':
  app.run(port=5000, debug=True) # Inicia o servidor na porta 5000. "Debug" é uma configuração para facilitar o desenvolvimento.
 
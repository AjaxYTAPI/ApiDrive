from flask import Flask, jsonify

data = [
    {
        "id": 1,
        "Nome": "Fulano",
        "Idade": 18
    },
    {
        "id": 2,
        "Nome": "Maria",
        "Idade": 26
    }
]

app = Flask(__name__)

@app.route("/")
def HomePage():
    return "<h1>Bem-vindo à minha API!</h1>"

@app.route("/api")
def api():
    return jsonify(data)

@app.route('/pesquisa/<int:id>', methods=['GET'])
def pesquisar(id):
    for i in data:
        if i["id"] == id:
            return jsonify(i)  # Retorna o item se encontrar pelo ID
    return jsonify({"erro": f"nenhum resultado com o id: {id}...."}), 404  # Retorna erro se não encontrar

# Rodar o servidor na porta padrão (5000) e disponível para todos
app.run(host="0.0.0.0", port=5000)

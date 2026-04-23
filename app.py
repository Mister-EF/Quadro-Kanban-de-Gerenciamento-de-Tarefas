from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tarefas = {
    "todo": ["Estudar Python", "Fazer café"],
    "doing": ["Projeto Kanban"],
    "done": ["Blog Markdown"]
}

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    global tarefas
    tarefas = request.json
    return jsonify({"status": "sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
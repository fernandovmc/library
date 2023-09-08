from flask import Flask, jsonify, request
import requests


app = Flask(__name__)
livros = [
    {
    'id': 1,
    'titulo': 'A Dança dos Dragões',
    'autor': 'George R. R. Martin',
    },
    {
    'id': 2,
    'titulo': '1984',
    'autor': 'George Orwell',
    },
    {
    'id': 3,
    'titulo': 'O Pequeno Príncipe',
    'autor': 'Antoine de Saint-Exupéry',
    },
    {
    'id': 4,
    'titulo': 'O Senhor dos Anéis: A Sociedade do Anel',
    'autor': 'J.R.R. Tolkien',
    },
    {
    'id': 5,
    'titulo': 'Dom Quixote',
    'autor': 'Miguel de Cervantes',
    },
    {
    'id': 6,
    'titulo': 'Cem Anos de Solidão',
    'autor': 'Gabriel García Márquez',
    },
    {
    'id': 7,
    'titulo': 'A Revolução dos Bichos',
    'autor': 'George Orwell',
    },
    {
    'id': 8,
    'titulo': 'O Alquimista',
    'autor': 'Paulo Coelho',
    },
    {
    'id': 9,
    'titulo': 'A Menina que Roubava Livros',
    'autor': 'Markus Zusak',
    },
    {
    'id': 10,
    'titulo': 'Crime e Castigo',
    'autor': 'Fiódor Dostoiévski',
    }
]

@app.route('/livros',methods=['GET'])
def get_livro():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def get_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>',methods=['PUT'])
def edit_livro(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate:
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros',methods=['POST'])
def add_livro():
    new_livro = request.get_json()
    livros.append(new_livro)
    return jsonify(livros)
    
@app.route('/livros/<int:id>',methods=['DELETE'])
def del_livro(id):
    for indice, livro in enumerate:
        if livro.get('id') == id:
            del livros[indice]
        
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)
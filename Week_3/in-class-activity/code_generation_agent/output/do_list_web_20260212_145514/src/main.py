import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for to-do items
todos = {}

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    if todo_id not in todos:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todos[todo_id])

@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400

    data = request.get_json()
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    todo_id = max(todos.keys()) + 1 if todos else 1
    todos[todo_id] = {
        'id': todo_id,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': data.get('completed', False)
    }
    return jsonify(todos[todo_id]), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id not in todos:
        return jsonify({'error': 'Todo not found'}), 404

    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400

    data = request.get_json()
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    todos[todo_id]['title'] = data['title']
    todos[todo_id]['description'] = data.get('description', todos[todo_id]['description'])
    todos[todo_id]['completed'] = data.get('completed', todos[todo_id]['completed'])
    return jsonify(todos[todo_id])

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id not in todos:
        return jsonify({'error': 'Todo not found'}), 404

    del todos[todo_id]
    return jsonify({'message': 'Todo deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

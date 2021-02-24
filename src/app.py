from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    # print("Incoming request with the following body", request_body)

    todos.append(decoded_object)
    lista_done=jsonify(todos)
    
    return  lista_done

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    new_list = jsonify(todos)
    return new_list 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
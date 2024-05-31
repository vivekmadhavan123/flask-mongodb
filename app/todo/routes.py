from flask import Blueprint, request

from app.todo import utils


todo_bp = Blueprint('todo', __name__, url_prefix='/todos')


@todo_bp.route('/get_todos', methods=['GET'])
def get_all_todos():
    todos = utils.get_all_todos()
    return {"data": todos}


@todo_bp.route('/<id>', methods=['GET'])
def get_todos_by_id(id):
    todos = utils.get_find_todo({"_id": id})
    return {"data": todos}


@todo_bp.route('/', methods=['POST'])
def insert_todo():
    payload = request.json
    utils.insert_todo(payload)
    return {"message": "Todo added successfully"}


@todo_bp.route('/<_id>', methods=['DELETE'])
def delete_todo(_id):
    utils.delete_todo_by_id(_id)
    return {"message": "Todo delete successfully"}

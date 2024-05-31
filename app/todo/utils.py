import json

from bson import json_util, ObjectId

from app import db


def parse_json(data):
    return json.loads(json_util.dumps(data))


def insert_todo(payload):
    db.todos.insert_one(payload)


def get_find_todo(query: dict):
    
    if "_id" in query:
        query["_id"] = ObjectId(query["_id"])
    todos = db.todos.find(query)
    return parse_json(todos) if todos else []


def get_all_todos():
    todos = db.todos.find()
    return parse_json(todos) if todos else []


def delete_todo_by_id(_id):
    db.todos.delete_one({"_id": ObjectId(_id)})

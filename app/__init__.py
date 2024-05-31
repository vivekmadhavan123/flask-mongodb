from flask import Flask, Blueprint
from pymongo import MongoClient


blue_print = Blueprint('api', __name__)

client = MongoClient('localhost', 27017)
db = client.TodoDB


def create_app():
    app = Flask(__name__)

    from app.todo.routes import todo_bp
    app.register_blueprint(todo_bp)
    return app

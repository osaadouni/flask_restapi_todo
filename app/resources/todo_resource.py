from flask_restful import reqparse, abort, Resource
from app.models.todo_model import TodoModel
from app import db

parser = reqparse.RequestParser()
parser.add_argument('task')

def abort_if_todo_doesnt_exist(todo_id):
    if not TodoModel.query.get(todo_id):
        abort(404, message="Todo {} doesn't exist".format(todo_id))

class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo = TodoModel.query.get(todo_id)
        return {'id': todo.id, 'task': todo.task}

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        todo = TodoModel.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        todo = TodoModel.query.get(todo_id)
        todo.task = args['task']
        db.session.commit()
        return {'task': todo.task}, 201

class TodoList(Resource):
    def get(self):
        todos = TodoModel.query.all()
        return [{'id': todo.id, 'task': todo.task} for todo in todos]

    def post(self):
        args = parser.parse_args()
        todo = TodoModel(args['task'])
        db.session.add(todo)
        db.session.commit()
        return {'task': todo.task, 'id': todo.id}, 201

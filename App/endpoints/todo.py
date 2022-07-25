from flask import request
from flask_restx import Resource, Namespace, fields
from App.models.todo import TodoModel
from App.schemas.todo import schema, list_schema

ns = Namespace('todos', description='Operations related to ToDos')

post_payload = ns.model('Todo', {
    'content': fields.String('Content of the ToDo', required=True),
    'completed': fields.Boolean('Flag if the ToDo is completed')
})

patch_payload = ns.model('Todo', {
    'content': fields.String('Content of the ToDo'),
    'completed': fields.Boolean('Flag if the ToDo is completed')
})

@ns.route('')
class TodoListController(Resource):
    def get(self):
        return list_schema.dump(TodoModel.all()), 200

    @ns.expect(post_payload)
    def post(self):
        todo = TodoModel.insert(request.get_json())
        return schema.dump(todo), 201

@ns.route('/<int:id>')
class TodoController(Resource):
    def get(self, id):
        return schema.dump(TodoModel.find_by_id(id)), 200

    @ns.expect(patch_payload)
    def patch(self, id):
        todo = TodoModel.update(id, request.get_json())
        return schema.dump(todo), 200

    def delete(self, id):
        TodoModel.delete(id)
        return "", 200
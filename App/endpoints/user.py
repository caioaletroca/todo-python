from flask import request
from flask_restx import Resource, Namespace, fields
from App.models.user import UserModel
from App.schemas.user import schema

ns = Namespace('users', description='Operations related to Users')

post_payload = ns.model('User', {
    'name': fields.String('User name', required=True),
    'email': fields.String('User e-mail', required=True),
    'password': fields.String('User password', required=True)
})

@ns.route('')
class UserListController(Resource):
    @ns.expect(post_payload)
    def post(self):
        user = UserModel.insert(request.get_json())
        return schema.dump(user), 201

@ns.route('/<int:id>')
class UserController(Resource):
    def get(self, id):
        return schema.dump(UserModel.find_by_id(id)), 200
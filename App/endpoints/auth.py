from flask import request
from flask_restx import Resource, Namespace, fields

ns = Namespace('login', description='Authentication operations')

@ns.route('')
class LoginController(Resource):
    def post(self):
        payload = request.get_json()
        print(payload)
        return 200
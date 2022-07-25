import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from App.restplus import api
from App.endpoints.todo import ns as ns_todo
from App.endpoints.user import ns as ns_user
from App.endpoints.auth import ns as ns_auth
from App.db import config_db
from App.ma import config_ma

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    api.init_app(app)

    config_db(app)
    config_ma(app)

    api.add_namespace(ns_todo)
    api.add_namespace(ns_user)
    api.add_namespace(ns_auth)
    
    if __name__ == "__main__":
        app.run(debug=True, port=os.getenv('PORT'))

    return app

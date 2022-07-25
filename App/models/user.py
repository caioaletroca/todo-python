import bcrypt
from sqlalchemy import event
from App.db import db
from App.models.base import BaseModel

class UserModel(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256))
    todos = db.relationship('TodoModel', backref='user', lazy=True)

    def __repr__(self) -> str:
        return f'<User {self.name}>'

@event.listens_for(UserModel.password, 'set', retval=True)
def before_insert_password(target, value, old_value, initiator):
    if value != old_value:
        return bcrypt.hashpw(str.encode(value), bcrypt.gensalt())

    return value

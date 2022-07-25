from App.db import db
from App.models.base import BaseModel

class TodoModel(BaseModel):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(256), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f'<Todo {self.content}>'
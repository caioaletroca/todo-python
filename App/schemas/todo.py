from App.ma import ma
from App.models.todo import TodoModel

class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TodoModel
        ordered = True

schema = TodoSchema()
list_schema = TodoSchema(many=True)
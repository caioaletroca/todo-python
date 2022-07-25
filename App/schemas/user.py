from App.ma import ma
from App.models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        ordered = True

schema = UserSchema()
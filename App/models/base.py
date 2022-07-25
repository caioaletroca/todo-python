from App.db import db

class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def insert(cls, payload):
        instance = cls(**payload)
        db.session.add(instance)
        db.session.commit()
        return instance

    @classmethod
    def update(cls, id, payload):
        instance = cls.find_by_id(id)
        
        for key, value in payload.items():
            setattr(instance, key, value)

        db.session.commit()
        return instance

    @classmethod
    def delete(cls, id):
        instance = cls.find_by_id(id)
        db.session.delete(instance)
        db.session.commit()
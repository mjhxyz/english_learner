from app.ext import db


class BaseModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns if c.name != '_sa_instance_state'}

    def __str__(self):
        return str(self.to_dict())

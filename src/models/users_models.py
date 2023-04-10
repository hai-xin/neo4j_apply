from src import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    age = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "age":self.age
        }

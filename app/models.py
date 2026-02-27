from flask_login import UserMixin
from . import db, bcrypt
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    def verify_password(self, password):
        return bcrypt.check_password_hash(self.hashed_password, password)
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.hashed_password = bcrypt.generate_password_hash(password)
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from blog.extensions import db, flask_bcrypt
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False, default="test@mail.ru", server_default="")
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    _password = Column(LargeBinary, nullable=False, default='')
    is_staff = Column(Boolean, nullable=False, default=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)

    def __repr__(self):
        return f'User - {self.username}'


# class Articles(db.Model):
#     __tablename__ = 'articles'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(255), unique=True, nullable=False)
#     description = Column(String)
#     author = relationship("User")
#
#     def __repr__(self):
#         return f'Article - {self.name_article}'
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from blog.extensions import db, flask_bcrypt
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False, default="test@mail.ru", server_default="")
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    _password = Column(LargeBinary, nullable=False, default='')
    is_staff = Column(Boolean, nullable=False, default=False)
    author = relationship('Author', uselist=False, back_populates='user')

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


class Author(db.Model):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='author')
    article = relationship('Articles', back_populates='author')


class Articles(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates='article')

    def __repr__(self):
        return f'Article - {self.name_article}'
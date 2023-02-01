from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from blog.models.database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(255), nullable=True)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'User - {self.username}'


# class Articles(db.Model):
#     __tablename__ = 'articles'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(255), unique=True, nullable=False)
#     description = Column(String)
#     author = relationship(User)
#
#     def __repr__(self):
#         return f'Article - {self.name_article}'
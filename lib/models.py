from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship , declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    posts = relationship('Post', back_populates='author')


class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    title = Column(String)
    content = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    date = Column(DateTime, default=datetime.utcnow)
    author = relationship('User', back_populates='posts')
    category = relationship('Category', back_populates='posts')



class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship('Post', back_populates='category')



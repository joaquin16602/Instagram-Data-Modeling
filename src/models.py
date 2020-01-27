import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250), nullable=False)
    user_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Descripcion = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # def to_dict(self):
    #     return {}



class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    liker_id = Column(Integer, ForeignKey('user.id'))
    date = Column(String(30))
    post = relationship(Post)
    user = relationship(User)
    
 


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(30), nullable=False)
    comment = Column(String(30), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user = relationship(User)
    date = Column(String(30))

class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

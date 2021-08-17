import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer(), unique=True, nullable=False) 
    commentor_id = Column(Integer(), unique= True, nullable=False)
    comment_text = Column(String(200), unique=False, nullable=False)
    created_at = Column(String(), unique=False, nullable=False)

    def to_dict(self):
        return {
        '<Comment %s>' % self.comments
        }


    def serialize(self):
        return {
            "id": self.id,
            "commentor": self.commentor_id,
            "text": self.comment_text,
            "date": self.created_at,
            
        }

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), unique=True, nullable=False)
    first_name = Column(String(), unique= True, nullable=False)
    last_name = Column(String(), unique=False, nullable=False)
    email = Column(String(), unique=False, nullable=False)
    password = Column(String(), unique=False, nullable=False)

    def to_dict(self):
        return {
        '<User %s>' % self.user
        }


    def serialize(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "password": self.password,
            
        }


class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), unique=True, nullable=False)
    title = Column(String(), unique= True, nullable=False)
    description = Column(String(), unique=False, nullable=False)
    media_source = Column(String(), unique=False, nullable=False)

    def to_dict(self):
        return {
        '<Post %s>' % self.posts
        }


    def serialize(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "title": self.title,
            "description": self.description,
            "mediaSource": self.media_source,
            
        }

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), unique=True, nullable=False)
    post_id = Column(String(), unique= True, nullable=False)
    liked_on = Column(String(), unique=False, nullable=False)

    def to_dict(self):
        return {
        '<Like %s>' % self.likes
        }


    def serialize(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "postId": self.post_id,
            "likedOn": self.liked_on,
            
        }


        

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
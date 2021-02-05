import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_text = Column(String(250), nullable=False)
    user_id = Column (Integer, ForeignKey('user.id'))
    media = relationship ("Media", back_populates="post")
    comments = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__ = 'comment    '
    id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=False)
    author = relationship("user", back_populates="post", lazy=True)
    post_id = Column (Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey('post.id'))
    url = Column(String(250), nullable=False)
    media_type = Column(String(250), nullable=False)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
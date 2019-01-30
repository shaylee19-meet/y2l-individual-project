from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Books (Base):
    __tablename__ = 'books'
    book_id=Column(Integer, primary_key=True)
    name_of_book=Column(String)
    author=Column(String)
    genre =Column(String)
    discription=Column(String) 
    pass

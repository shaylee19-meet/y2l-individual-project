from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_book (name_of_book, author, genre,description ):
    book= Books(name_of_book=name_of_book, author=author, genre=genre, discription=description)
    session.add(book)
    session.commit()

def all_books():
    books=session.query(Books).all()
    return books



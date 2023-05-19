from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class AuthorBook (Base):
    __tablename__= "author_book"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    title = Column(String, ForeignKey('book.title'))
    book = relationship('Book', back_populates='authors')
    def __init__(self, name, title):
        self.name = name
        self.title = title


class Book (Base):
    __tablename__= "book"
    title = Column(String, primary_key=True)
    description = Column(String)
    publisher = Column(String)
    publishedDate = Column(Date)
    categories = Column(String)
    ratingsCount=Column(Float)
    ratings = relationship('Rating', back_populates='book')
    authors = relationship('AuthorBook', back_populates='book')
    def __init__(self, title, description, publisher, publishedDate, categories, ratingsCount):
        self.title = title
        self.description = description
        self.publisher = publisher
        self.publishedDate = publishedDate
        self.categories = categories
        self.ratingsCount = ratingsCount


class Rating (Base):
    __tablename__= "rating"
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    score = Column(Float)
    time = Column(Integer)
    summary = Column(String)
    text = Column(String)
    title = Column(String, ForeignKey('book.title'))
    book = relationship('Book', back_populates='ratings')
    def __init__(self, title, price, score, time, summary, text):
        self.title = title
        self.price = price
        self.score = score
        self.time = time
        self.summary = summary
        self.text = text

def create_tables():
    host = "publisher.cikmh2zvbh8u.us-east-1.rds.amazonaws.com"
    port = '5432'
    user = 'postgres'
    password = 'postgres'
    database = 'publisher'

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}', echo=False)    
    print('Creando tablas en la base de datos..')
    Base.metadata.create_all(engine)
    print('Tablas creadas exitosamente..')

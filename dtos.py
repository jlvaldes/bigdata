from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, MetaData, Table
from global_variables import DB_HOST, DB_PASS, DB_PORT, DB_USER, DB_DATABASE


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
    publishedDate = Column(String)
    categories = Column(String)
    ratingsCount=Column(Float)
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
    title = Column(String)
    def __init__(self, title, price, score, time, summary, text):
        self.title = title
        self.price = price
        self.score = score
        self.time = time
        self.summary = summary
        self.text = text

def create_tables():
    engine = get_engine()
    print('Creando tablas en la base de datos..')
    Base.metadata.create_all(engine)
    print('Tablas creadas exitosamente..')

def get_engine():
    host = DB_HOST
    port = DB_PORT
    user = DB_USER
    password = DB_PASS
    database = DB_DATABASE

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}', echo=False)   
    return engine 

def delete_all_data(table_name):
    print(f'Eliminando datos de la tabla {table_name}')
    engine = get_engine()
    conexion = engine.connect()
    metadata = MetaData(bind=engine)
    tabla = Table(table_name, metadata, autoload=True)
    delete_statement = tabla.delete()
    conexion.execute(delete_statement)
    conexion.close()
    print(f'Tabla {table_name} vacía...')


if __name__ == '__main__':
    create_tables()
import pandas as pd
from global_variables import CSV_BOOK_DATA_CLEANED_PATH, CSV_BOOK_DATA_PATH
from global_variables import CSV_BOOK_RATING_CLEANED_PATH, CSV_BOOK_RATING_PATH
from dtos import Book, Rating, AuthorBook
import os
from dtos import get_engine, delete_all_data
from sqlalchemy.orm import sessionmaker


def to_dtos(data_cleaned = False, df_data = None, df_rating = None):
    books = []
    authors = []
    ratings = []
    
    
    if df_data.empty :
        pd.set_option('display.max_colwidth', None)
        if data_cleaned == False:
            ruta_data_csv = CSV_BOOK_DATA_PATH
        else:
            ruta_data_csv = CSV_BOOK_DATA_CLEANED_PATH

        ruta_data_absoluta = os.path.abspath(ruta_data_csv)

        df_data = pd.read_csv(ruta_data_absoluta)
        print('Dataset de libros cargado...')

    if df_rating.empty:
        pd.set_option('display.max_colwidth', None)
        if data_cleaned == False:
            ruta_rating_csv = CSV_BOOK_RATING_PATH
        else:
            ruta_rating_csv = CSV_BOOK_RATING_CLEANED_PATH

        ruta_rating_absoluta = os.path.abspath(ruta_rating_csv)

        df_rating = pd.read_csv(ruta_rating_absoluta)
        print('Dataset de rating cargado...')


    for index, row in df_data.iterrows():
        book = Book(title= row['Title'], 
            description= row['description'], 
            publisher= row['publisher'], 
            categories= row['categories'], 
            ratingsCount= row['ratingsCount'],
            publishedDate= row['publishedDate'])

        authors_errors = 0
        if row['authors'] != None:
            try:
                authors_name = eval(str(row['authors']))
                for author in authors_name:
                    authors.append(
                        AuthorBook(name=author, title= book.title)
                    )
            except:
                authors_errors += 1
        
        books.append(book)
    
    for index, row in df_rating.iterrows():
        ratings.append(
            Rating(title= row['Title'], 
                price= row['Price'], 
                score= row['review/score'],
                time= row['review/time'], 
                summary=row['review/summary'],
                text= row['review/text'])
        )

    return books, authors, ratings


def load():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    books, authors, ratings = to_dtos()
    delete_all_data('book')
    print("Cargar libros...")
    session.add_all(books[:10])
    session.commit()
    session.close()
    print("Libros cargados...")


#Retorna una lista de objetos DTOs para cargar a la base de datos 
def transform_data(data_cleaned = False, df1 = None, df2 = None):
    print('Transformando los datos del CSV a un modelo sqlalchemy...')
    books, authors, ratings =  to_dtos(data_cleaned, df_data= df1, df_rating= df2)
    print('Transformación finalizada...')
    return books, authors, ratings



